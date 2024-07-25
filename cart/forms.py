from django import forms
from django.conf import settings

# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, getattr(settings, 'CART_MAX_QUANTITY', 20) + 1)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int
    )
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )
