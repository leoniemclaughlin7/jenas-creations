from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import CustomOrder
from profiles.models import UserProfile
from .forms import CustomOrderForm
from django.contrib import messages


def custom_order(request):
    """ A view to display custom_order form """
    if request.method == 'POST':
        custom_form = CustomOrderForm(request.POST)
        if custom_form.is_valid():
            custom = custom_form.save(commit=False)
            user_profile = UserProfile.objects.get(user=request.user)
            custom.user_profile = user_profile
            custom.save()
            messages.success(request, f'Your custom order has been added to your bag. Price: Eur{custom.price}')
            return redirect(reverse('price'))
    else:
        custom_form = CustomOrderForm()

    context = {
        'custom_form': custom_form,
    }

    return render(request, 'custom_order/custom_order.html', context)

 
def custom_order_details(request):
    user_profile = UserProfile.objects.get(user=request.user)
    custom_order = get_object_or_404(CustomOrder, user_profile=user_profile)
    price = custom_order.price
    context = {
        'price': price,
        'custom_order': custom_order,
    }

    return render(request, 'custom_order/custom_order_price.html', context)

def add_custom_order_to_bag(request, custom_order_id):
    """ Add a quantity of the specified product to the shopping bag """
    custom_order = CustomOrder.objects.get(pk=custom_order_id)
    bag = request.session.get('bag', {})

    bag['custom_order'] = custom_order_id
   
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))