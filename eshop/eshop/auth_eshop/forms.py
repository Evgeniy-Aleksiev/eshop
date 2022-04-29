from django.contrib.auth import get_user_model
from django.contrib.auth import forms

from eshop.core.mixins import BootstrapFormMixin

UserModel = get_user_model()


class RegisterForm(BootstrapFormMixin, forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email', )


class LoginForm(BootstrapFormMixin, forms.AuthenticationForm):
    user = None

    def clean_password(self):
        super().clean()
        self.user = authenticate(
            email=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )

        if not self.user:
            raise ValidationError('Email and/or password incorrect')

    def save(self):
        return self.user