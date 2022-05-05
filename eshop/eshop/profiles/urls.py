from django.urls import path

from eshop.profiles import views

urlpatterns = [
    path('<int:pk>/', views.ProfileShowView.as_view(), name='profile'),
    path('<int:pk>/update/', views.ProfileEditView.as_view(), name='profile edit'),
]