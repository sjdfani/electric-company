from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    PanelAdditionalDocumentViewSet, PanelOperatorViewSet,
    PanelSuggestionViewSet, PanelTypeOfDamageViewSet,
    PanelUsersViewSet, PanelDamageReportsViewSet
)

router = DefaultRouter()
router.register('users', PanelUsersViewSet, basename='user')
router.register('damage-reports', PanelDamageReportsViewSet,
                basename='damage-report')
router.register('additional-documents',
                PanelAdditionalDocumentViewSet, basename='additional-document')
router.register('type-of-damages', PanelTypeOfDamageViewSet,
                basename='type-of-damage')
router.register('operators', PanelOperatorViewSet, basename='operator')
router.register('suggestions', PanelSuggestionViewSet, basename='suggestion')

urlpatterns = router.urls
