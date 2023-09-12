import datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Get the current year for the max value validator
current_year = datetime.date.today().year

# Create your models here.
class Category(models.Model):
    name_categ = models.CharField(max_length=50)
    visible=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.name_categ
    
class Brand(models.Model):
    name_brand = models.CharField(max_length=50)
    visible=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name_brand

class Product(models.Model):
    name_product = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    model_year = models.PositiveIntegerField(
        validators=[ 
            MinValueValidator(1900, message="Year must be greater than or equal to 1900"),
            MaxValueValidator(current_year, message=f"Year must be less than or equal to {current_year}")
        ]
    )
    images_product = models.ImageField(upload_to='Products/images/')
    stock = models.PositiveIntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    