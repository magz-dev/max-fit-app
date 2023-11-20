from django import template

# Register a template filter called 'calc_subtotal'

register = template.Library()

""" Template filter to calculate the subtotal."""

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity