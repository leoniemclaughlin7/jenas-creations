from django import forms
from .models import CustomOrder
from products.models import Category


class CustomOrderForm(forms.ModelForm):

    class Meta:
        model = CustomOrder
        fields = ('category', 'material', 'colour_scheme',
                  'charm', 'personalised',
                  'name', 'additional_details')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        self.fields['category'].widget.attrs['autofocus'] = True