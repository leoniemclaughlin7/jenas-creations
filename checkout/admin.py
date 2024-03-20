from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Initiating readonly fields for order lineitem.
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Order admin set up, using list display
    so as admin panel will be ordered by the display
    below and ordering so admin can easily find
    orders.
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'grand_total',)

    list_display = ('order_number', 'date', 'full_name',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
