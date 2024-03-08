from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product

def view_bag(request):
    """
    A view to return bag page
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, product_id):
    """ Add a quantity of the specified product to the shopping bag """
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    
    bag = request.session.get('bag', {})

    if product_id in list(bag.keys()):
        bag[product_id] += quantity
        messages.success(
                request, f'Updated {product.name} quantity to {bag[product_id]}')
    else:
        bag[product_id] = quantity
        messages.success(request, f'{product.name} has been added to your bag!')

    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag(request, product_id):
    bag = request.session.get('bag', {})
    quantity = int(request.POST.get('quantity'))
    if product_id == str(1000):
        if 'custom_order' in bag:
            custom_order_id = bag['custom_order']
            return redirect(reverse('custom_order_update', args=[custom_order_id, quantity]))
            
    if quantity > 0:
        bag[product_id] = quantity
        messages.success(
                request, f'Updated {product.name} quantity to {bag[product_id]}')
    else:
        bag.pop(product_id, None)
        messages.success(request, f'Removed {product.name} from your bag')
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def remove_from_bag(request, product_id):
    bag = request.session.get('bag', {})

    if product_id == str(1000):
        if 'custom_order' in bag:
            custom_order_id = bag['custom_order']
            return redirect(reverse('custom_order_delete', args=[custom_order_id]))

    bag.pop(product_id)
    messages.success(request, f'Removed {product.name} from your bag')
    
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))