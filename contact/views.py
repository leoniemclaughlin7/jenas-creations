from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.contrib import messages


def contact(request):
    """ A view to display contact form """
    if request.method == 'POST':
        contact = ContactForm(request.POST)
        if contact.is_valid():
            contact.save()
            messages.success(request, 'Your message has been sent, please expect a response via email.')
            contact = ContactForm()
    else:
        contact = ContactForm()

    context = {
        'contact': contact,
    }

    return render(request, 'contact/contact.html', context)
