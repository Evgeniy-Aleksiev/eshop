from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixin, get_user_model

from eshop.main.forms import ContactUsForm

UserModel = get_user_model()


class HomePageView(views.TemplateView):
    template_name = 'main/home_page.html'


class AboutUsView(views.TemplateView):
    template_name = 'main/about_us.html'


class ContactsView(views.CreateView):
    template_name = 'main/contacts.html'
    form_class = ContactUsForm

    def get_success_url(self):
        return reverse_lazy('contact message')


class ContactsMessageView(views.TemplateView):
    template_name = 'main/contact_message.html'
