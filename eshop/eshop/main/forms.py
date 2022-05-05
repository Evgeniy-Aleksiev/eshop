from django import forms

from eshop.core.mixins import BootstrapFormMixin
from eshop.main.models import ContactUs


class ContactUsForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = ContactUs
        fields = '__all__'
