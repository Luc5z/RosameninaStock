from django import forms
from .models import Product, Sale

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['nome', 'marca', 'categoria', 'cor', 'preco', 'descricao', 'quantidade', 'imagem', 'naloja']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Produto'}),
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Marca'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categoria'}),
            'cor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cor'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Preço', 'step': '0.01'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descrição do Produto'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'naloja': forms.CheckboxInput(attrs={'class': 'form-check-input ms-1'}),
        }


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['quantidade', 'cliente', 'email', 'pagamento', 'preco_unitario']
        widgets = {
            'cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Cliente'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail do Cliente'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'preco_unitario': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}), 
            'pagamento': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        produto = kwargs.pop('produto', None)
        super().__init__(*args, **kwargs)

        if produto:
            self.fields['preco_unitario'].initial = produto.preco
            self.fields['quantidade'].widget.attrs['max'] = produto.quantidade


