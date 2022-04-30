from django.urls import path

from eshop.main import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
]