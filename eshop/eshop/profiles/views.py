from django.shortcuts import render
from django.contrib.auth import mixins as auth_mixin
from django.urls import reverse_lazy

from django.views import generic as views

from eshop.profiles.forms import ProfileUpdateForm
from eshop.profiles.models import Profile


def profile_update(request):
    profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

    if profile_form.is_valid():
        profile_form.save()

    context = {
        'profile_form': profile_form,
    }

    return render(request, 'auth/profile-update.html', context)