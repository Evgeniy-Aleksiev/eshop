from django.urls import path
from eshop.products import views

urlpatterns = [
    path('products/', views.ProductsView.as_view(), name='products'),

]