from django import forms
from ..DEMOAPP.templates.account import *


class Login(forms.Form):
    password = forms.CharField(widget=forms.TextInput
                               (attrs={'id': 'passw'}))
