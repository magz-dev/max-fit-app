from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order

def profile(request):
    """ Display the user's profile. """
    
    # Retrieve the user's profile or return a 404 error if not found
    profile = get_object_or_404(UserProfile, user=request.user)

    # Check if the form is submitted through a POST request
    if request.method == 'POST':
        # Create a form instance with the submitted data and the user's profile as an instance
        form = UserProfileForm(request.POST, instance=profile)
        
        # Check if the form is valid
        if form.is_valid():
            # Save the form data to update the user's profile
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            # Display an error message if the form is not valid
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        # If the request is not a POST request, create a form instance with the user's profile
        form = UserProfileForm(instance=profile)
    
    # Retrieve all orders associated with the user's profile
    orders = profile.orders.all()

    # Set the template and context for rendering the profile page
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    # Render the profile page with the specified template and context
    return render(request, template, context)


def order_history(request, order_number):
    """ Display the order history for a specific order number. """
    
    # Retrieve the order with the given order number or return a 404 error if not found
    order = get_object_or_404(Order, order_number=order_number)

    # Display an informational message about the past order confirmation
    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    # Set the template and context for rendering the order history page
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    # Render the order history page with the specified template and context
    return render(request, template, context)
