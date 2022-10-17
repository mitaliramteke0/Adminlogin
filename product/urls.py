from django.contrib import admin
from django.urls import path
from rest_framework.templatetags.rest_framework import data

from product.views import ProductApiView

urlpatterns = [
    path('product/', admin.site.urls),
    path('api/',ProductApiView.as_view),
    path('edit/',data),
    path('delete/',data),

]