from django.urls import path
from .views import (
    CreateDamageReportView, ListTypeOfDamagesView, RetrieveDamageReportView,
)

app_name = 'damage'

urlpatterns = [
    path('create/', CreateDamageReportView.as_view(), name='damage-reports'),
    path('type-of-damages/', ListTypeOfDamagesView.as_view(), name='type-of-damages'),
    path('track/', RetrieveDamageReportView.as_view(), name='track'),
]
