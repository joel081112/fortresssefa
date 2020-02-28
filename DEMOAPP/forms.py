from django import forms
from ..DEMOAPP.templates.account import *
from .models import Product


class Login(forms.Form):
    password = forms.CharField(widget=forms.TextInput
                               (attrs={'id': 'passw'}))


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'Description',
        ]