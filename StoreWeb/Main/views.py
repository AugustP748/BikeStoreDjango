from django.shortcuts import render
from Products.models import Product, Category
# Create your views here.
def home(request):
    context = {}
    context['list_products']=Product.objects.all()
    context['list_categories']=Category.objects.all()
    return render(request, 'home.html',context = context)