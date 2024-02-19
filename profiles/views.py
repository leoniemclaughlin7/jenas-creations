from django.shortcuts import render, get_object_or_404
from .models import User


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(User, user=request.user)

    context = {
        'profile': profile,
    }

    return render(request, 'profiles/profile.html', context)
