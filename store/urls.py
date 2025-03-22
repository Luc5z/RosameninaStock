from django.urls import path
from . import views
from .views import ProductListView, ProductDetailView, SaleCreateView, SaleListView, SaleDetailView

urlpatterns = [
    path('inicio/', ProductListView.as_view(), name='ProductListView'),
    path('produto/<int:pk>', ProductDetailView.as_view(), name='productview'),
    path('venda/<int:product_id>/', SaleCreateView.as_view(), name='sale'),
    path('vendas/', SaleListView.as_view(), name='saleList'),

    
    # path('search/', views.search, name='search'),
    # path('productview/', views.productView, name='productView'),
    # path('checkout/', views.checkout, name='checkout'),
]




