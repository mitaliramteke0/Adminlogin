from django import forms
from django.contrib.auth.forms import UserCreationForm

from product.models import Product


class ChangeProdForm(Product):
    class Meta:
        model = Product
        fields = "__all__"
