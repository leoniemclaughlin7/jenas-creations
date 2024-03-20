from django.urls import path
from . import views

urlpatterns = [
    path('', views.custom_order, name='custom_order'),
    path('price/<int:custom_order_id>/', views.custom_order_details,
         name='price'),
    path('add_custom_order/<int:custom_order_id>/',
         views.add_custom_order_to_bag, name='add_custom_order'),
    path('update_custom_order/<int:custom_order_id>/<int:quantity>',
         views.custom_order_update, name='custom_order_update'),
    path('delete_custom_order/<int:custom_order_id>/',
         views.custom_order_delete, name='custom_order_delete'),
]
