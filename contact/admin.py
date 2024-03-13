from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    """
    Contact admin set up, using list display
    so as admin panel will be ordered by the display
    below and list filter so admin can easily find
    messages.  
    """
    list_display = (
        'full_name',
        'email',
        'created_on',
    )
    list_filter = ('full_name', 'email', 'created_on')

admin.site.register(Contact, ContactAdmin)
