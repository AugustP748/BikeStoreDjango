
class Cart:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {} 
        self.cart = cart
            
    def Add_to_cart(self,product):
        if (str(product.id) not in self.cart.keys()):
            self.cart[product.id] = {
                "product_id": product.id,
                "product_name": product.name_product,
                "price": str(product.price),
                "subtotal": str(product.price),
                "images_product": product.images_product.url,
                "quantity": 1
            }
        else:
            for key, value in self.cart.items():
                if key == str(product.id):
                    value["quantity"] = value["quantity"] + 1 
                    value["subtotal"] = float(value["subtotal"]) + float(value["price"])
                    break
                
        self.Save_cart()
        
    def Save_cart(self):
        self.session["cart"] = self.cart
        self.session.modified = True
        
    def Delete_item(self,product):
        product.id=str(product.id)
        if product.id in self.cart:
            del self.cart[product.id]
            self.Save_cart()
    
    def Subtract_units(self,product):
        for key, value in self.cart.items():
            if key == str(product.id):
                value["quantity"] = value["quantity"] - 1 
                value["subtotal"] = float(value["subtotal"]) - float(value["price"])
                if value["quantity"] < 1:
                    self.Delete_item(product)
                break
        self.Save_cart()

    def Clear_cart(self):
        self.session["cart"] = {}
        self.session.modified = True