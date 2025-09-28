from django.urls import path
from shop.views import (
    IndexView, CategoryDetailView, ProductDetailView, DiscountedProductListView,
    ProductListView, CreateProductView, UpdateProductView, DeleteProductView
)

app_name='shop'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('specific_category/<int:category_pk>/', CategoryDetailView.as_view(), name='specific_categories'),
    path('product/<int:product_pk>/', ProductDetailView.as_view(), name='product'),
    path('discounted/', DiscountedProductListView.as_view(), name='discounted_product'),
    path('all_products/', ProductListView.as_view(), name='all_products'),
    path('add_product/', CreateProductView.as_view(), name='add_product'),
    path('update_product/<int:product_pk>/', UpdateProductView.as_view(), name='update_product'),
    path('delete_product/<int:product_pk>/', DeleteProductView.as_view(), name='delete_product'),
]