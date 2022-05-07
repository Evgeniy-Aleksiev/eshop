from django.contrib import admin

from eshop.profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', )
    readonly_fields = ('user', )

