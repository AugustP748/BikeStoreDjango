from django.urls import path
from .views import ProductDetailView
from django.conf.urls.static import static
from django.conf import settings

app_name="Products"
urlpatterns = [
    path('detail/<int:pk>',ProductDetailView.as_view(),name='productDetail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)