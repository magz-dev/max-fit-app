from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        # Define the fields to be included in the form
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
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

        # Loop through form fields to set placeholders and classes
        for field in self.fields:
            # Exclude 'country' field from the loop
            if field != 'country':
            # Add '*' to the placeholder if the field is required
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]

                # Set placeholder attribute
                self.fields[field].widget.attrs['placeholder'] = placeholder

            # Add a custom class to the form field for styling
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            
            # Remove auto-generated labels for form fields
            self.fields[field].label = False