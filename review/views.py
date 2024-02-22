from django.shortcuts import render
from .models import Review
from .forms import Review

def review(request):
    """
    A view to return index page 
    """
    reviews = Review.objects.order_by('-created_on').all()
    if request.method == 'POST':
        review_form = Review(request.POST)

        if review_form.is_valid():
            review_form.instance.name = request.user.username
            review_form.save()
            review_form = Review()
            messages.add_message(request, messages.SUCCESS,
                                 'Your review has been successfully posted!')
    else:
        review_form = Review()

    context = {
        'review_form': review_form, 
    }    

    return render(request, 'product/product_detail.html', context)
