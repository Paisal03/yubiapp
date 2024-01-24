from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_vegetarian = models.CharField(max_length=100)

    

    def __str__(self):
        return self.name

# Create your models here.
