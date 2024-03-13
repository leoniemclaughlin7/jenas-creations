from django.contrib import admin
from .models import CustomOrder


class CustomOrderAdmin(admin.ModelAdmin):
    """
    Custom order admin set up, using list display
    so as admin panel will be ordered by the display
    below and list filter so admin can easily find
    orders.  
    """
    list_display = (
        'material',
        'category',
        'price',
        'created_on',
    )
    list_filter = ('material', 'category', 'created_on')

admin.site.register(CustomOrder, CustomOrderAdmin)


