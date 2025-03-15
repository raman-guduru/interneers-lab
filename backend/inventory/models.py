from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=255)
    brand = models.CharField(max_length=255,default="Generic")
    price = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0)])
    quantity = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name