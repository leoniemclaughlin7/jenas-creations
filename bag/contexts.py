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

    print(bag)
     
    if 'custom_order' in bag:
        custom_order_id = bag['custom_order'] 
        custom_order = CustomOrder.objects.get(pk=custom_order_id)
        if 'quantity' in bag:
            total += bag['quantity'] * custom_order.price
            individual_total = bag['quantity'] * custom_order.price
            bag_items.append({
                'product_id': custom_order.product_id,
                'custom_order_id': custom_order_id,
                'category': custom_order.category,
                'material': custom_order.material,
                'individual_total': individual_total,
                'quantity': bag['quantity'],
                'product_name': custom_order.product_name,
                'price': custom_order.price,
         })
        else:
            total += custom_order.price
            bag_items.append({
                'product_id': custom_order.product_id,
                'custom_order_id': custom_order_id,
                'category': custom_order.category,
                'material': custom_order.material,
                'individual_total': custom_order.price,
                'quantity': 1,
                'product_name': custom_order.product_name,
                'price': custom_order.price,
            })
        

    for product_id, quantity in bag.items():
        if product_id == 'custom_order' or product_id == str(1000) or product_id == 'quantity': 
            continue
        product = Product.objects.get(pk=product_id)
        if isinstance(quantity, int) and isinstance(product.price, Decimal):
            total += quantity * product.price
            individual_total = quantity * product.price
            product_count += quantity
            bag_items.append({
            'product_id': product_id,
            'quantity': quantity,
            'product': product,
            'individual_total': individual_total,
        })
    
    grand_total = total
    

    context = {
        'bag_items': bag_items,
        'grand_total': grand_total,
        'product_count': product_count
    }

    return context