from django.urls import path
from . import views

urlpatterns = [
    path('', views.custom_order, name='custom_order'),
]