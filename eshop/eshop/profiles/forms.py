from django import forms

from eshop.core.mixins import BootstrapFormMixin
from eshop.profiles.models import Profile


class ProfileUpdateForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name']
