from django.contrib import admin
from .models import Suggestion


class SuggestionAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ('user',)


admin.site.register(Suggestion, SuggestionAdmin)
