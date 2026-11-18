from django.urls import path
from . import views

urlpatterns = [
    path('Products/GetAll', views.api_get_all_products, name='api_get_all_products'),
    path('Products/GetFiltered', views.api_get_filtered_products, name='api_get_filtered_products'),
    path('Categories/GetAll', views.api_get_all_categories, name='api_get_all_categories'),
    path('Categories/GetCategory/<int:id>', views.api_get_category, name='api_get_category'), 
    path('Baskets/GetAll', views.api_get_all_basket_items, name='api_get_all_basket_items'),
    path('Baskets/DeleteProduct/<int:id>', views.api_delete_basket_product, name='api_delete_basket_product'),
    path('Messages/GetAll', views.api_get_all_messages, name='api_get_all_messages'),
        
]