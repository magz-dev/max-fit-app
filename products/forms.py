# Import necessary modules from Django
from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category

# Create a form for handling Product model data
class ProductForm(forms.ModelForm):
    # Meta class to specify the model and fields for the form
    class Meta:
        model = Product
        fields = '__all__'
    
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    # Constructor to initialize the form with additional customizations
    def __init__(self, *args, **kwargs):
        # Call the parent class constructor
        super().__init__(*args, **kwargs)

        # Retrieve all Category objects from the database
        categories = Category.objects.all()

        # Create a list of tuples containing category IDs and their friendly names
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # Set the choices for the 'category' field to the list of friendly names
        self.fields['category'].choices = friendly_names

        # Add custom attributes to form fields for styling
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)