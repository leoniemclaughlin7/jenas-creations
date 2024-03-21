from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product, Category
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from review.models import Review
from review.forms import ReviewForm
from contact.models import Contact
from django.db.models import Avg


def all_products(request):
    """
    A view to show all products. Sorting products by category,
    search querys and sorting products by price.
    """
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
                queries = Q(name__icontains=search_query) | \
                          Q(description__icontains=search_query)
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
    """
    A view to display product details. Also displays
    review form, reviews and avg_rating.
    """

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.order_by('-created_on').filter(
                                        product_id=product_id)
    avg_rating = Review.objects.filter(product_id=product_id).aggregate(
                                        avg_stars=Avg('stars'))
    rating = avg_rating['avg_stars']

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.product_id = product_id
            review.name = request.user.username
            review.save()
            review_form = ReviewForm()
            messages.add_message(request, messages.SUCCESS,
                                 'Your review has been successfully posted!')
    else:
        review_form = ReviewForm()

    context = {
        'product': product,
        'review_form': review_form,
        'reviews': reviews,
        'rating': rating
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    Add a product to the store and display contact messages
    """
    if not request.user.is_superuser:
        messages.error(request, 'Request denied! You do not have '
                       'authorisation to add products.')
        return redirect(reverse('home'))

    contact = Contact.objects.order_by('-created_on').all()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure '
                           'the form is valid.')
    else:
        form = ProductForm()

    context = {
        'form': form,
        'contact': contact
    }

    return render(request, 'products/add_product.html', context)


@login_required
def edit_product(request, product_id):
    """
     Edit a product in the store
     """
    if not request.user.is_superuser:
        messages.error(request, 'Request denied! You do not have '
                       'authorisation to edit products.')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please '
                           'ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'products/edit_product.html', context)


@login_required
def delete_product(request, product_id):
    """
    Delete a product from the site
    """
    if not request.user.is_superuser:
        messages.error(request, 'Request denied! You do not have '
                       'authorisation to delete products.')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
