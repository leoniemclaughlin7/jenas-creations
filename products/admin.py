from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """
    Product admin set up, using list display
    so as admin panel will be ordered by the display
    below. 
    """
    list_display = (
        'name',
        'category',
        'price',
        'image',
    )
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
