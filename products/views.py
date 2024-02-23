from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product, Category
from django.contrib import messages
from django.db.models import Q
from .forms import ProductForm

def all_products(request):
    """ A view to show all products """

    products = Product.objects.all()
    categories = None
    search_query = None

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
            search_query = request.GET['query']
            if search_query:
                queries = Q(name__icontains=search_query) | Q(description__icontains=search_query)
                products = products.filter(queries)
            else:
                messages.error(request, "Please enter search criteria!")
                return redirect(reverse('products'))
    

    context = {
        'products': products,
        'current_categories': categories,
        'search_query': search_query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to display product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

 
def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            individual_total
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
    
    context = {
        'form': form,
    }
 
    return render(request, 'products/add_product.html', context)

def edit_product(request, product_id):
    """ Edit a product in the store """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'products/edit_product.html', context)