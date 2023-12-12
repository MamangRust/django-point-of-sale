from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control"})
    )
    price = forms.DecimalField(
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    image = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control"}))
    quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Product
        fields = ["name", "description", "price", "image", "quantity"]
