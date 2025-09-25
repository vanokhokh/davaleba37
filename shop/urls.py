from django.urls import path
from shop.views import index, specific_categories, product, discounted_product, all_products, add_product

app_name='shop'

urlpatterns = [
    path('', index, name='home'),
    path('<int:category_pk>/', specific_categories, name='specific_categories'),
    path('<int:product_pk>/', product, name='product'),
    path('discounted/', discounted_product, name='discounted_product'),
    path('all_products/', all_products, name='all_products'),
    path('add_product/', add_product, name='add_product'),
]