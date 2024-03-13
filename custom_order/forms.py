from django import forms
from .models import CustomOrder
from products.models import Category


class CustomOrderForm(forms.ModelForm):

    class Meta:
        """
        CustomOrderForm initiation using the CustomOrder model.
        Sets fields as below.
        """
        model = CustomOrder
        fields = ('category', 'material', 'colour_scheme',
                  'charm', 'personalised',
                  'name', 'additional_details')


    def __init__(self, *args, **kwargs):
        """
        Gets all the categories and sets autofocus on category field.
        """
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        self.fields['category'].widget.attrs['autofocus'] = True