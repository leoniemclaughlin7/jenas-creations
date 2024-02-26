from django.urls import path
from . import views

urlpatterns = [
    path('', views.custom_order, name='custom_order'),
    path('price/', views.custom_order_details, name='price'),
]