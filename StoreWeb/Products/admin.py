from django.contrib import admin
from .models import Product,Category,Brand

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name_categ", "created", "updated","visible"]
    
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["name_brand", "created", "updated","visible"]
    
@admin.register(Product)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["name_product", "price", "model_year","stock","brand","category"]