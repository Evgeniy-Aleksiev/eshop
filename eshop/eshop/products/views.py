from django.shortcuts import render
from django.views import generic as views

from eshop.products.models import Product


class ProductsView(views.ListView):
    model = Product
    template_name = 'products/product.html'
