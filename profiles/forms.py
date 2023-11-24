from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # Exclude the 'user' field from the form
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Custom initialization method to add placeholders, classes,
        remove auto-generated labels, and set autofocus on the first field.
        """
        super().__init__(*args, **kwargs)
        # Define placeholders for form fields
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State, or Locality',
        }

        # Set autofocus on the 'default_phone_number' field
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True

        # Iterate through form fields to add placeholders, classes, and modify labels
        for field in self.fields:
            if field != 'default_country':
                # Set a placeholder with an asterisk for required fields
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder

                # Add custom classes to the form input fields
                self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'

            # Remove auto-generated labels
            self.fields[field].label = False
