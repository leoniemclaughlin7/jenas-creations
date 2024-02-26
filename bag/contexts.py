from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from custom_order.models import CustomOrder

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for product_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=product_id)
        total += quantity * product.price
        individual_total = quantity * product.price
        product_count += quantity
        bag_items.append({
            'product_id': product_id,
            'quantity': quantity,
            'product': product,
            'individual_total': individual_total,
        })

    if 1000 in bag.items():
        custom_order_id = bag[1000]
        custom_order = get_object_or_404(CustomOrder, pk=custom_order_id)
        total += custom_order.price
        bag_items.append({
            'product_id': 1000,
            'quantity': 1,
            'product': custom_order,
            'individual_total': custom_order.price,
        })
        product_count += 1
    
    grand_total = total
    

    context = {
        'bag_items': bag_items,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context