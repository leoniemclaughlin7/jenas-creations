from django.shortcuts import render
from .forms import Review

def review(request):
    """
    A view to return index page 
    """
    return render(request, 'review/review.html')
