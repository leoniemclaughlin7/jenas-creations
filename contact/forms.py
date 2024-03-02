from .models import Contact
from django import forms


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('full_name', 'email', 'message')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs['autofocus'] = True