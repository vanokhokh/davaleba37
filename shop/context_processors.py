from shop.models import Product

def last_created(request):
    last_5_product = Product.objects.order_by('-created')[:5]

    return {
        'last_5_product': last_5_product,
    }