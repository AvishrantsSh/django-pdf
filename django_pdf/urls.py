from django.contrib import admin
from django.urls import path

from django_pdfview.views import Home

urlpatterns = [
    path("", Home, name="home"),
    path("admin/", admin.site.urls),
]
