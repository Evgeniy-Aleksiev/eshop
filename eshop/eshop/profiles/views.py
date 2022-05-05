from django.contrib.auth import mixins as auth_mixin, get_user_model

from django.views import generic as views

from eshop.profiles.models import Profile

UserModel = get_user_model()


class ProfileShowView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = Profile
    template_name = 'profiles/show-profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ProfileEditView(auth_mixin.LoginRequiredMixin, views.UpdateView):
    model = Profile
