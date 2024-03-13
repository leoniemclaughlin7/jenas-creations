from django.contrib import admin
from .models import Review


admin.site.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Review admin set up, using list display
     and list filter so admin
    can filter the reviews by number of stars and date.
    """
    list_display = ('name', 'stars', 'created_on')
    list_filter = ('stars', 'created_on')