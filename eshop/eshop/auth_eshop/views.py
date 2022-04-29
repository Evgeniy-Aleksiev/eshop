from django.contrib.auth import views as auth_views
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views import generic as views

from eshop.auth_eshop.forms import RegisterForm, LoginForm

UserModel = get_user_model()


class RegisterView(views.CreateView):
    template_name = 'auth/register.html'
    model = UserModel
    form_class = RegisterForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'Activate your account.'
        message = render_to_string('auth/activate_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        return render(self.request, 'auth/activation_need.html')


class LoginView(auth_views.LoginView):
    template_name = 'auth/login.html'
    form_class = LoginForm
    redirect_field_name = 'next'


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_encode(uidb64).decode()
        user = UserModel.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_verified = True
        user.save()
        return render(request, 'auth/login.html', {"form": LoginForm})
    else:
        return render(request, 'auth/activation_invalid.html')
