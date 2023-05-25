from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=105)
    slug = models.SlugField(unique=True)
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to="product", null=True)
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE)
