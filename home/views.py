from django.shortcuts import render

def index(request):
    """
    A view to return index page 
    """
    bag = request.session.get('bag', {})
    show_custom_order_link = True

    if 'custom_order' in bag:
        show_custom_order_link = False

    context = {
        'show_custom_order_link': show_custom_order_link
    }
    return render(request, 'home/index.html', context)
