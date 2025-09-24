from django.shortcuts import render
from django.db.models import Count
from shop.models import Category, Product


def index(request):
    all_category = Category.objects.annotate(total_products=Count('products'))
    return render(request, 'index.html', {'all_category':all_category})

def specific_categories(request, category_pk):
    category_id = Category.objects.get(pk=category_pk)
    all_product = Product.objects.filter(category=category_id)
    return render(request, 'specific_categories.html', {'category_id':category_id , 'all_product':all_product})

def product(request, product_pk):
    product_id = Product.objects.get(pk=product_pk)
    return render(request, 'product.html', {'product_id':product_id})

def discounted_product(request):
    discount = Product.objects.filter(discount=True)
    return render(request, 'discounted.html', {'discount':discount})