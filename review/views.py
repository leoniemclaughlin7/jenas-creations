from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def edit_review(request, review_id):
    """ Edit a product in the store """
    review = get_object_or_404(Review, pk=review_id)
    if str(request.user) != review.name:
        messages.error(request, 'Request denied! You do not have authorisation to edit this review.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated review!')
            return redirect('product_detail', product_id=review.product.id)
        else:
            messages.error(request, 'Failed to update review. Please ensure the form is valid.')
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing a review posted by {review.name}')

    context = {
        'form': form,
        'review': review,
    }

    return render(request, 'review/edit_review.html', context)
