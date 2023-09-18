from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name="Carts"
urlpatterns = [
    path('add/<int:product_id>',views.add_product,name="add_cart"),
    path('delete/<int:product_id>',views.delete_product,name="delete_cart"),
    path('substract/<int:product_id>',views.substrat_product,name="substract_cart"),
    path('clear-cart/',views.clear_card,name="clear_cart"),
    path('items-cart/',views.items_cart,name="items_cart"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)