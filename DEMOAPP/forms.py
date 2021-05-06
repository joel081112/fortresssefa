from django import forms
from .models import Product, Type


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = '__all__'

