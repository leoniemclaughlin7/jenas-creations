from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product, Category
from django.contrib import messages
from django.db.models import Q

def all_products(request):
    """ A view to show all products """

    products = Product.objects.all()
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        
        if 'sort' in request.GET:
            sort_key = request.GET['sort']
            if sort_key == 'price':
                products = products.order_by('price')
            else:
                products = products.order_by('-price')

        if 'query' in request.GET:
            searchQuery = request.GET['query']
            if searchQuery:
                queries = Q(name__icontains=searchQuery) | Q(description__icontains=searchQuery)
                products = products.filter(queries)
            else:
                messages.error(request, "Please enter search criteria!")
                return redirect(reverse('products'))
    

    context = {
        'products': products,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to display product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)