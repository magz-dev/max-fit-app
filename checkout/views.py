from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    # If the shopping bag is empty, display an error message and redirect to the products page
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    # Create an instance of the OrderForm
    order_form = OrderForm()

    # Define the template for the checkout page
    template = 'checkout/checkout.html'

    # Context to be passed to the template
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OFfLbIgz7mgrzCgkTEHXHHFb2tSqnHmhDG3tcrHf2NJpF5sbgfYGjjMpxdsukLFxLOyyZI7h0IIj1AWKz7HNGfn00S66WgfBJ'
    }
    # Render the checkout page with the order form
    return render(request, template, context)