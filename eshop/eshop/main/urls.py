from django.urls import path

from eshop.main import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('about-us/', views.AboutUsView.as_view(), name='about us'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('feedback/', views.FeedbackView.as_view(), name='feedback'),
]