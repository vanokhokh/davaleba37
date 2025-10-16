from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count, Q
from unicodedata import category

from shop.models import Category, Product
from shop.forms import ProductForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class IndexView(ListView):
    model = Category
    template_name = 'index.html'
    context_object_name = 'category'
    queryset = Category.objects.annotate(total_products=Count('products'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_5_product'] = Product.objects.order_by('-id')[:5]
        return context

class CategoryDetailView(ListView):
    model = Product
    template_name = 'specific_categories.html'
    context_object_name = 'all_products'
    paginate_by = 5

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['category_pk'])
        return Product.objects.filter(category=self.category).select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

class ProductListView(ListView):
    model = Product
    template_name = 'all_product.html'
    context_object_name = 'all_products'
    ordering = ['price']
    paginate_by = 4

    def get_queryset(self):
        products = Product.objects.all().select_related('category')

        search_q = self.request.GET.get('q')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')

        if search_q:
            products = products.filter(Q(title__icontains=search_q) | Q(description__icontains=search_q))
        if min_price:
            products = products.filter(price__gte=min_price)
        if max_price:
            products = products.filter(price__lte=max_price)

        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product.html'
    pk_url_kwarg = 'product_pk'

class DiscountedProductListView(ListView):
    model = Product
    template_name = 'discounted.html'
    context_object_name = 'discounted_products'
    queryset = Product.objects.filter(discount=True)
    paginate_by = 4

class CreateProductView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = '/all_products/'

class UpdateProductView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'update_product.html'
    pk_url_kwarg = 'product_pk'

    def get_success_url(self):
        return reverse_lazy('shop:product' , kwargs={'product_pk':self.object.pk})

class DeleteProductView(LoginRequiredMixin, DeleteView):
    model = Product
    pk_url_kwarg = 'product_pk'
    success_url = '/all_products/'
