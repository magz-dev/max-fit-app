from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        # Define the fields to include in the form
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels, and set autofocus on the first field
        """
        super().__init__(*args, **kwargs)
        # Define placeholders for form fields
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        # Set autofocus on the first field
        self.fields['full_name'].widget.attrs['autofocus'] = True

        # Iterate through form fields to set placeholders and classes
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    # Add * to the placeholder for required fields
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                # Set placeholder attribute for the field
                self.fields[field].widget.attrs['placeholder'] = placeholder

            # Set the CSS class for styling
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            
            # Remove auto-generated labels
            self.fields[field].label = False
