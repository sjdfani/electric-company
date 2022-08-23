from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin
from users.models import User
from .serializer import (
    PanelAdditionalDocumentSerializer, PanelDamageReportSerializer,
    PanelOperatorSerializer, PanelTypeOfDamageSerializer,
    PanelUserSerializer
)
from .permissions import IsSuperuser, IsAdminOrSuperUser
from damage.models import DamageReport, TypeOfDamage, AdditionalDocument
from suggestion.serializer import SuggestionSerializer
from suggestion.models import Suggestion


class PanelUsersViewSet(ModelViewSet):
    permission_classes = [IsAdminOrSuperUser]
    serializer_class = PanelUserSerializer
    queryset = User.objects.filter(is_staff=False).order_by('-date_joined')


class PanelDamageReportsViewSet(
    GenericViewSet, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin
):
    permission_classes = [IsAdminOrSuperUser]
    serializer_class = PanelDamageReportSerializer
    queryset = DamageReport.objects.order_by('-created_at', '-pk')


class PanelAdditionalDocumentViewSet(
    GenericViewSet, CreateModelMixin, DestroyModelMixin, RetrieveModelMixin
):
    permission_classes = [IsSuperuser]
    serializer_class = PanelAdditionalDocumentSerializer
    queryset = AdditionalDocument.objects.order_by('-pk')


class PanelTypeOfDamageViewSet(ModelViewSet):
    permission_classes = [IsSuperuser]
    serializer_class = PanelTypeOfDamageSerializer
    queryset = TypeOfDamage.objects.order_by('-pk')


class PanelOperatorViewSet(ModelViewSet):
    permission_classes = [IsSuperuser]
    serializer_class = PanelOperatorSerializer
    queryset = User.objects.filter(
        is_superuser=False, is_staff=True).order_by('full_name')


class PanelSuggestionViewSet(
    GenericViewSet, RetrieveModelMixin, DestroyModelMixin, ListModelMixin
):
    permission_classes = [IsSuperuser]
    serializer_class = SuggestionSerializer
    queryset = Suggestion.objects.order_by('-pk')
