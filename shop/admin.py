from django.contrib import admin
from django.db.models import F
from shop.models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'discount', 'category']
    list_display_links = ['title']
    actions = ('make_discount_true','make_discount_false', 'minus_price')

    @admin.action(description="make discount True")
    def make_discount_true(self, request, queryset):
        queryset.update(discount=True)

    @admin.action(description="make discount False")
    def make_discount_false(self, request, queryset):
        queryset.update(discount=False)

    @admin.action(description="get price less 10 percent")
    def minus_price(self, request, queryset):
        queryset.update(price=F('price') * 0.9)