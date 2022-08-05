from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import User


class MyUserAdmin(UserAdmin):
    list_display = ['phone_number', 'full_name']
    search_fields = ['phone_number', 'full_name']
    ordering = ['full_name']
    fieldsets = (
        (_('Personal information'), {
            'fields': ('phone_number', 'full_name', 'national_code', 'province', 'city', 'postal_code', 'address', 'api_key', 'password')
        }),
        (_('Date information'), {
            'fields': ('date_joined', 'last_login')
        }),
        (_('Other information'), {
            'fields': ('is_staff', 'is_active', 'is_superuser', 'user_permissions')
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'phone_number', 'full_name', 'national_code', 'province', 'city', 'postal_code', 'address'
            )
        }),
    )


admin.site.register(User, MyUserAdmin)
