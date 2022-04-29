from django.urls import path

from eshop.auth_eshop import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]