from django import forms
from .models import Product, Sale

class ProductForm(forms.ModelForm):
    onstore = forms.BooleanField(required=False, widget=forms.CheckboxInput())

    class Meta:
        model = Product
        fields = ['name', 'category', 'subcategory', 'price', 'description', 'quantity', 'image', 'onstore']

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['quantity', 'client', 'email', 'payment', 'unit_price']
        widgets = {
            'client': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Cliente'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail do Cliente'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}), 
            'payment': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        product = kwargs.pop('product', None)
        super().__init__(*args, **kwargs)

        if product:
            self.fields['unit_price'].initial = product.price
            self.fields['quantity'].widget.attrs['max'] = product.quantity


