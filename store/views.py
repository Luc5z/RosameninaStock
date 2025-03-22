from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Sale
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

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
    template_name = 'saleCreate.html'
    fields = ['quantity', 'client', 'email']  # Campos necessários no formulário

    def get_initial(self):
        """Preenche o formulário com os dados do produto"""
        initial = super().get_initial()
        product_id = self.kwargs.get('product_id')  # Pegando da URL
        if product_id:
            product = get_object_or_404(Product, id=product_id)
            initial['product'] = product  # Aqui já pode configurar a inicialização com o produto
        return initial

    def get_context_data(self, **kwargs):
        """Adiciona o produto ao contexto do template"""
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs.get('product_id')
        context['product'] = get_object_or_404(Product, id=product_id)
        return context

    def form_valid(self, form):
        """Processa o formulário e salva a venda"""
        product = get_object_or_404(Product, id=self.kwargs['product_id'])
        
        # Atualiza a quantidade do produto
        quantity = form.cleaned_data['quantity']
        if quantity > product.quantity:
            form.add_error('quantity', 'Quantidade solicitada é maior que a disponível.')
            return self.form_invalid(form)
        
        product.quantity -= quantity
        product.save()

        # Cria e salva a venda
        sale = form.save(commit=False)
        sale.product = product
        sale.total_price = product.price * quantity  # O preço total depende da quantidade
        sale.save()

        # Redireciona para a lista de vendas após salvar
        return super().form_valid(form)

    def get_success_url(self):
        """Define a URL de sucesso após o cadastro da venda"""
        return reverse_lazy('saleList')  # Certifique-se de que o nome da URL está correto

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