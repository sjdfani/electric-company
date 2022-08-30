from django.contrib import admin
from .models import DamageReport, TypeOfDamage


class DamageReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'billing_id', 'date_time', 'done_date')
    list_filter = ('user', 'type_of_damage', 'status')


class TypeOfDamageAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(DamageReport, DamageReportAdmin)
admin.site.register(TypeOfDamage, TypeOfDamageAdmin)
