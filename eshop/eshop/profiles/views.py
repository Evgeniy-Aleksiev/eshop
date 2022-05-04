from django.contrib.auth import mixins as auth_mixin, get_user_model, update_session_auth_hash
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import generic as views
from django.views.generic.detail import SingleObjectMixin

from eshop.auth_eshop.forms import UserUpdateForm
from eshop.profiles.forms import ProfileUpdateForm
from eshop.profiles.models import Profile

UserModel = get_user_model()


class ProfileShowView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = UserModel
    template_name = 'profiles/show-profile.html'
    object = None

    def get(self, request, *args, **kwargs):
        self.object = self.model.objects.get(pk=self.kwargs["pk"])
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.object
        return context


def profile_and_user_update(request):
    user_form = UserUpdateForm(instance=request.user)
    profile_form = ProfileUpdateForm(instance=request.user.profile)
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            update_session_auth_hash(request, request.user)
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'profiles/update-profile.html', context)