from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category_photo', null=True, blank=True, default='def.jpg')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'

class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='product_photo', null=True, blank=True, default='def.jpg')

    def __str__(self):
        return self.title

    class Meta:
        db_table = "product"


