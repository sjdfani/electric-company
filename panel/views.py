from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from users.models import User
from .serializer import (
    PanelAdditionalDocumentSerializer, PanelDamageReportSerializer,
    PanelOperatorSerializer, PanelTypeOfDamageSerializer,
    PanelUserSerializer
)
from .permissions import IsSuperuser, IsStaffOrSuperuser
from damage.models import DamageReport, TypeOfDamage, AdditionalDocument
from suggestion.serializer import SuggestionSerializer
from suggestion.models import Suggestion


class PanelUsersViewSet(ModelViewSet):
    permission_classes = [IsStaffOrSuperuser]
    serializer_class = PanelUserSerializer
    queryset = User.objects.filter(is_staff=False).order_by('-date_joined')


class PanelDamageReportsViewSet(
    GenericViewSet, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin
):
    permission_classes = [IsAuthenticated]
    serializer_class = PanelDamageReportSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return DamageReport.objects.order_by('-created_datetime', '-pk')
        elif self.request.user.is_staff and not self.request.user.is_superuser:
            lookup = Q(operator=None) | Q(operator=self.request.user)
            return DamageReport.objects.filter(lookup).order_by('-created_datetime', '-pk')
        elif not (self.request.user.is_staff and self.request.user.is_superuser):
            return DamageReport.objects.filter(user=self.request.user).order_by('-created_datetime', '-pk')


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
    permission_classes = [IsAuthenticated]
    serializer_class = SuggestionSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Suggestion.objects.order_by('-pk')
        return Suggestion.objects.filter(user=self.request.user).order_by('-pk')
