from django.urls import path, include
from main.views import index, about, menu, contact, cart, add_to_cart, increase_quantity, decrease_quantity, remove_from_cart

app_name = 'restaurant'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('menu/', menu, name='menu'),
    path('contact/', contact, name='contact'),
        
    # Shopping cart
    path('cart/', cart, name='cart'),
    path('add-to-cart/<int:dish_id>/', add_to_cart, name='add_to_cart'),
    path('increase-quantity/<int:item_id>/', increase_quantity, name='increase_quantity'),
    path('decrease-quantity/<int:item_id>/', decrease_quantity, name='decrease_quantity'),
    path('remove-from-cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    
   
]