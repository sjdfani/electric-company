from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin
from users.models import User
from .serializer import (
    PanelAdditionalDocumentSerializer, PanelDamageReportSerializer,
    PanelOperatorSerializer, PanelSuggestionSerializer,
    PanelTypeOfDamageSerializer, PanelUserSerializer
)
from .permissions import APIKeyPermission
from damage.models import *


class PanelUsersViewSet(ModelViewSet):
    permission_classes = [APIKeyPermission]
    serializer_class = PanelUserSerializer
    queryset = User.objects.order_by('-date_joined')


class PanelDamageReportsViewSet(
    GenericViewSet, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin
):
    serializer_class = PanelDamageReportSerializer
    queryset = DamageReport.objects.order_by('-created_at', '-pk')


class PanelAdditionalDocumentViewSet(
    GenericViewSet, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin
):
    serializer_class = PanelAdditionalDocumentSerializer
    queryset = AdditionalDocument.objects.order_by('-pk')


class PanelTypeOfDamageViewSet(ModelViewSet):
    serializer_class = PanelTypeOfDamageSerializer
    queryset = TypeOfDamage.objects.order_by('-pk')


class PanelOperatorViewSet(ModelViewSet):
    serializer_class = PanelOperatorSerializer
    queryset = Operator.objects.order_by('full_name')


class PanelSuggestionViewSet(
    GenericViewSet, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin
):
    serializer_class = PanelSuggestionSerializer
    queryset = Suggestion.objects.order_by('-pk')
