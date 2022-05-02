from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from eshop.main.forms import FeedbackForm


class HomePageView(views.TemplateView):
    template_name = 'main/home_page.html'


class AboutUsView(views.TemplateView):
    template_name = 'main/about_us.html'


class ContactsView(views.TemplateView):
    template_name = 'main/contacts.html'


class FeedbackView(views.CreateView):
    template_name = 'main/feedback.html'
    form_class = FeedbackForm

    def get_success_url(self):
        return reverse_lazy('feedback message')
