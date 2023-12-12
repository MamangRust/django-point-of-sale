from django import forms


class PaymentForm(forms.Form):
    cartNumber = forms.CharField(required=True, max_length=16)
    expirationDate = forms.CharField(required=True, max_length=5)
    paymentMethod = forms.CharField(required=True, max_length=17)
    cvv = forms.CharField(required=True, max_length=3)
    user = forms.IntegerField()

    amount = forms.DecimalField(max_digits=10, decimal_places=2)
