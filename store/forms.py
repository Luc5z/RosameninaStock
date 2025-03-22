from .models import Store, Sale
from django import forms

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'category', 'subcategory', 'price', 'description', 'quantity', 'image', 'onstore']

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['quantity', 'price', 'date', 'client', 'email']