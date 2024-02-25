from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    """
    Review form set up
    """
    class Meta:
        model = Review
        fields = ('stars', 'body')