from django.contrib import admin

from eshop.main.models import ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'date', 'message', )
    list_filter = ('date', 'name', )
    search_fields = ('date', 'email', 'name')
