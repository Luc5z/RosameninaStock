from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Sale
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .forms import SaleForm, ProductForm

class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'productview.html'
    context_object_name = 'product'

class SaleCreateView(CreateView):
    model = Sale
    form_class = SaleForm
    template_name = 'saleCreate.html'
    success_url = reverse_lazy('ProductListView')  # Ajuste conforme necessário

    def get_initial(self):
        """Preenche o formulário com os dados do produto"""
        initial = super().get_initial()
        product_id = self.kwargs.get('product_id')
        if product_id:
            product = get_object_or_404(Product, id=product_id)
            initial['unit_price'] = product.price  # Preenchendo o preço unitário
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs.get('product_id')
        context['product'] = get_object_or_404(Product, id=product_id)
        return context

    def form_valid(self, form):
        product = get_object_or_404(Product, id=self.kwargs['product_id'])
        quantity = form.cleaned_data['quantity']

        if quantity > product.quantity:
            form.add_error('quantity', 'Quantidade solicitada é maior que a disponível.')
            return self.form_invalid(form)

        # Reduz estoque
        product.quantity -= quantity
        product.save()

        # Salva venda
        sale = form.save(commit=False)
        sale.product = product
        sale.unit_price = product.price
        sale.total_price = product.price * quantity

        print(f"Salvando venda: {sale.client}, {sale.email}, {sale.quantity}, {sale.unit_price}, {sale.total_price}")

        sale.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('saleList')

class SaleListView(ListView):
    model = Sale
    template_name = 'saleList.html'
    context_object_name = 'sales'

class SaleDetailView(DetailView):
    model = Sale
    template_name = 'saleview.html'
    context_object_name = 'sale'


    
# class ProductCreateView(CreateView):
#     model = Product
#     template_name = 'product_form.html'
#     fields = '__all__'