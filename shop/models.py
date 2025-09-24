from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'category'

class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    discount = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    def __str__(self):
        return self.title
    class Meta:
        db_table = "product"


