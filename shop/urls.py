from django.urls import path
from shop.views import index, specific_categories, product, discounted_product, all_products, add_product, update_product, delete_product

app_name='shop'

urlpatterns = [
    path('', index, name='home'),
    path('specific_category/<int:category_pk>/', specific_categories, name='specific_categories'),
    path('product/<int:product_pk>/', product, name='product'),
    path('discounted/', discounted_product, name='discounted_product'),
    path('all_products/', all_products, name='all_products'),
    path('add_product/', add_product, name='add_product'),
    path('update_product/<int:product_id>/', update_product, name='update_product'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
]