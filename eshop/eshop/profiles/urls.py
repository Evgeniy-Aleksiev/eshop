from django.urls import path

from eshop.profiles import views

urlpatterns = [
    path('update/', views.profile_update, name='profile update'),
]