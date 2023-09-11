from django.contrib import admin
from django.urls import path, include

app_name="Login"
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("django.contrib.auth.urls")),
]