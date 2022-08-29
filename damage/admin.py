from django.contrib import admin
from .models import DamageReport


class DamageReportAdmin(admin.ModelAdmin):
    list_display = ('user',)


admin.site.register(DamageReport, DamageReportAdmin)
