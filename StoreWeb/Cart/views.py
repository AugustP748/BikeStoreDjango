from django.http import HttpResponseRedirect
from django.shortcuts import redirect,render
from Products.models import Product
from .cart import Cart

# Create your views here.
def add_product(request,product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.Add_to_cart(product)
    #return HttpResponseRedirect(request.path_info)
    return redirect("Main:home")


def delete_product(request,product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.Delete_item(product)
    return redirect("Main:home")

def substrat_product(request,product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.Subtract_units(product)
    return redirect("Main:home")

def clear_card(request):
    cart = Cart(request)
    cart.Clear_cart()
    return redirect("Main:home")

def items_cart(request):
    return render(request,'itemsCart.html')