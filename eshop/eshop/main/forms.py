from django import forms

from eshop.core.mixins import BootstrapFormMixin
from eshop.main.models import Feedback


class FeedbackForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Feedback
        fields = '__all__'
