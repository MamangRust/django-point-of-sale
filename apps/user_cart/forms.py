from django import forms
from .models import UserCart


class UserCartForm(forms.Form):
    user = forms.IntegerField()
    product = forms.IntegerField()
    quantity = forms.IntegerField()
