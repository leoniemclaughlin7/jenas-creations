from django.shortcuts import render, redirect, reverse

def view_bag(request):
    """
    A view to return bag page
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, product_id):
    """ Add a quantity of the specified product to the shopping bag """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    
    bag = request.session.get('bag', {})

    if product_id in list(bag.keys()):
        bag[product_id] += quantity
    else:
        bag[product_id] = quantity

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
    else:
        bag.pop(product_id, None)
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def remove_from_bag(request, product_id):
    bag = request.session.get('bag', {})
    bag.pop(product_id)
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))