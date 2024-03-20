from .models import Contact
from django import forms


class ContactForm(forms.ModelForm):

    class Meta:
        """
        Sets up the ContactForm using the contact model.
        Fields include full_name, email and message.
        """
        model = Contact
        fields = ('full_name', 'email', 'message')

    def __init__(self, *args, **kwargs):
        """
        Sets autofocus on full_name field
        """
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs['autofocus'] = True
