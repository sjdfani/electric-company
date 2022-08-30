from django.contrib import admin
from .models import DamageReport, TypeOfDamage, AdditionalDocument


class DamageReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'billing_id', 'date_time', 'done_date')
    list_filter = ('user', 'type_of_damage', 'status')


class TypeOfDamageAdmin(admin.ModelAdmin):
    list_display = ('title',)


class AdditionalDocumentAdmin(admin.ModelAdmin):
    list_display = ('damage_report',)


admin.site.register(DamageReport, DamageReportAdmin)
admin.site.register(TypeOfDamage, TypeOfDamageAdmin)
admin.site.register(AdditionalDocument, AdditionalDocumentAdmin)
