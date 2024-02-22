class Review(forms.ModelForm):
    """
    Review form set up
    """
    class Meta:
        model = Review
        fields = ('stars', 'body')