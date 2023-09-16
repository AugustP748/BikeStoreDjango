from django.shortcuts import render
from django.views.generic import DetailView
from .models import Product

# Create your views here.
class ProductDetailView(DetailView):
    template_name = 'products/Productdetail.html'
    model = Product
