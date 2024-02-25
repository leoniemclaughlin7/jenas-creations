from django.shortcuts import render
from .models import CustomOrder
from .forms import CustomOrderForm


def custom_order(request):
    """ A view to display custom_order form """
    custom_form = CustomOrderForm()

    context = {
        'custom_form': custom_form,
    }

    return render(request, 'custom_order/custom_order.html', context)


