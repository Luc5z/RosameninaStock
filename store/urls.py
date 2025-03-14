from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('search/', views.search, name='search'),
    # path('productview/', views.productView, name='productView'),
    # path('checkout/', views.checkout, name='checkout'),
]




