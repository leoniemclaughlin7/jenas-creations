from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from checkout.models import Order


@login_required
def profile(request):
    """
    A view to get users profile. If request method is post save user
    profile form. Also returns all users orders with the most recent
    first.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Failed to update. Please ensure the '
                           'form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all().order_by('-date')

    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, 'profiles/profile.html', context)


def order_history(request, order_number):
    """
    A view to return the order history for a specific users order.
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
  