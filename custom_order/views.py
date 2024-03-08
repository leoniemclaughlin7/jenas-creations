from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import CustomOrder
from .forms import CustomOrderForm
from django.contrib import messages


def custom_order(request):
    """ A view to display custom_order form """
    if request.method == 'POST':
        custom_form = CustomOrderForm(request.POST)
        if custom_form.is_valid():
            custom = custom_form.save(commit=False)
            custom.save()
            custom_order_id = custom.pk
            messages.success(request, f'Your custom order has been added to your bag. Price: Eur{custom.price}')
            return redirect(reverse('price', args=[custom_order_id]))
    else:
        custom_form = CustomOrderForm()

    context = {
        'custom_form': custom_form,
    }

    return render(request, 'custom_order/custom_order.html', context)

 
def custom_order_details(request, custom_order_id):
    custom_order = CustomOrder.objects.get(pk=custom_order_id)
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
    messages.success(
                request, 'Added custom order to your bag.')
   
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def custom_order_update(request, custom_order_id, quantity):
    bag = request.session.get('bag', {})
    value = custom_order_id
    if value in bag.values():
        if int(quantity) > 0:
            bag['quantity'] = quantity
            messages.success(
                request, f'Updated custom order quantity to {quantity}')
        
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def custom_order_delete(request, custom_order_id):
    bag = request.session.get('bag', {})
    value = custom_order_id
    if value in bag.values():
        del bag['custom_order']
        messages.success(request, 'Removed custom order from your bag')
    if 'quantity' in bag:
        del bag['quantity']
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

