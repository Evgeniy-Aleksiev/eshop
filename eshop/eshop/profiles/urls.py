from django.urls import path

from eshop.profiles import views

urlpatterns = [
    path('<int:pk>/', views.ProfileShowView.as_view(), name='profile'),
    path('update/', views.profile_and_user_update, name='profile update'),
]