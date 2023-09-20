

def Total_cart(request):
    total:int = 0
    if request.user.is_authenticated:
        try:
            if request.session["cart"]:
                for key,value in request.session["cart"].items():
                    total = total + float(value["subtotal"])
        except Exception:
            ...

    return {"total_cart":total}