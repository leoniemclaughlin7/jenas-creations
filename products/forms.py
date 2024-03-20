from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        """
        Set up product form, includes all fields.
        """
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Gets all categories.
        """
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
