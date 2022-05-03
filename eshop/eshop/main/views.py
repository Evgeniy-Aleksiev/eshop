from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixin, get_user_model

from eshop.main.forms import FeedbackForm

UserModel = get_user_model()


class HomePageView(views.TemplateView):
    template_name = 'main/home_page.html'


class AboutUsView(views.TemplateView):
    template_name = 'main/about_us.html'


class ContactsView(views.TemplateView):
    template_name = 'main/contacts.html'


class FeedbackView(auth_mixin.LoginRequiredMixin, views.CreateView):
    template_name = 'main/feedback.html'
    form_class = FeedbackForm
    context_object_name = UserModel

    def get_success_url(self):
        return reverse_lazy('feedback message')


class FeedbackMessageView(auth_mixin.LoginRequiredMixin, views.CreateView):
    template_name = 'main/feedback_message.html'
