from django.contrib.auth import mixins as auth_mixin, get_user_model, logout
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse

from django.views import generic as views

from eshop.profiles.models import Profile

UserModel = get_user_model()


class ProfileShowView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = Profile
    template_name = 'profiles/show_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ProfileEditView(auth_mixin.LoginRequiredMixin, views.UpdateView):
    model = Profile
    template_name = 'profiles/profile.html'
    fields = ('first_name', 'last_name', 'mobile_number', )

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.user.id})


class ProfileDeleteView(auth_mixin.LoginRequiredMixin, views.DeleteView):
    model = UserModel
    template_name = 'profiles/profile_delete.html'

    def get_success_url(self):
        logout(self.request)
        return reverse('index')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect('profile', self.request.user.id)
        return super().post(request, *args, **kwargs)
