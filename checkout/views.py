# Import necessary modules and classes from Django 
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
# Import models, forms, and context from current and related apps
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from bag.contexts import bag_contents
# Import modules for payment processing
import stripe
import json

# Define a view to handle the caching of checkout data using Stripe
@require_POST
def cache_checkout_data(request):
    try:
        # Extract payment intent ID from the client secret
        pid = request.POST.get('client_secret').split('_secret')[0]
        # Set the Stripe API key and modify the PaymentIntent metadata
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        # Return a success response
        return HttpResponse(status=200)
    except Exception as e:
        # Handle exceptions and return an error message
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)

# Define the checkout view
def checkout(request):
    # Get Stripe public and secret keys from settings
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        # Process the form data when the request method is POST
        bag = request.session.get('bag', {})
        # Extract form data from the request
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
         # Create an order form instance with the extracted form data
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            # Save the order with the provided form data and associate it with the PaymentIntent ID
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()

            # Process individual items in the bag and create corresponding OrderLineItem instances
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    # Handle the case where a product in the bag is not found in the database
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            # Set session variable to indicate whether user wants to save info
            request.session['save_info'] = 'save-info' in request.POST
            # Redirect to the checkout success page with the order number as an argument
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            # Handle the case where the order form is not valid
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        # Retrieve bag from session and display an error message if it is empty
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        # Calculate total, convert to stripe format, and create a PaymentIntent
        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        # Create an empty order form
        order_form = OrderForm()

    if not stripe_public_key:
        # Display a warning message if the Stripe public key is missing
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    # Define the template and context for rendering the checkout page
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    # Render the checkout page
    return render(request, template, context)

# Define a view to handle successful checkouts
def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    # Retrieve save_info from session and get the corresponding order
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    # Display a success message with the order number
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')
    # Clear the bag from the session
    if 'bag' in request.session:
        del request.session['bag']

    # Define the template and context for rendering the checkout success page
    template = 'checkout/checkout_success.html'
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    
    # Render the checkout success page
    return render(request, template, context)