from django.shortcuts import render
from django.http import HttpResponse


# from django.views.generic import ListView
# # from .models import Product

# class ProductListView(ListView):
#     model = Product
#     template_name = 'product_list.html'
#     context_object_name = 'products'

def index(request):
    return render(request, 'index.html')