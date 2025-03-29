from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Sale
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .forms import SaleForm, ProductForm
from django.contrib import messages


class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Product.objects.filter(nome__icontains=query)
        return Product.objects.all()

class ProductDetailView(DetailView):
    model = Product
    template_name = 'productview.html'
    context_object_name = 'product'

class SaleCreateView(CreateView):
    model = Sale
    form_class = SaleForm
    template_name = 'saleCreate.html'

    def get_initial(self):
        initial = super().get_initial()
        product_id = self.kwargs.get('product_id')
        if product_id:
            product = get_object_or_404(Product, id=product_id)
            initial['preco_unitario'] = product.preco 
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs.get('product_id')
        context['product'] = get_object_or_404(Product, id=product_id)
        return context

    def form_valid(self, form):
        product = get_object_or_404(Product, id=self.kwargs['product_id'])
        quantidade = form.cleaned_data['quantidade']

        messages.success(self.request, "Venda realizada com sucesso!")

        # Reduz estoque
        product.quantidade -= quantidade
        product.save()

        sale = form.save(commit=False)
        sale.produto = product
        sale.preco_unitario = product.preco
        sale.valor_total = product.preco * quantidade

        sale.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('saleList')

class SaleListView(ListView):
    model = Sale
    template_name = 'saleList.html'
    context_object_name = 'sales'
    paginate_by = 8

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Sale.objects.filter(cliente__icontains=query)
        return Sale.objects.all()

class SaleDetailView(DetailView):
    model = Sale
    template_name = 'saleview.html'
    context_object_name = 'sale'

class ProductCreateView(CreateView):
    model = Product
    template_name = "productCreate.html"
    form_class = ProductForm
    success_url = reverse_lazy("productCreate")  

    def form_valid(self, form):
        messages.success(self.request, "Produto criado com sucesso!")  # ✅ Mensagem de sucesso
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Erro ao cadastrar o produto. Verifique os dados.")  # ❌ Mensagem de erro
        return super().form_invalid(form)