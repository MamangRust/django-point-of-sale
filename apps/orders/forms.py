from django import forms


class OrderCreateForm(forms.Form):
    user_id = forms.IntegerField()
    product_id = forms.IntegerField()
    payment_id = forms.IntegerField()
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    quantity = forms.IntegerField()
