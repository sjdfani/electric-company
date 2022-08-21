from rest_framework.response import Response
from damage.models import DamageReport, TypeOfDamage
# from .serializer import (
#     # CreateDamageReportSerializer, RetrieveDamageReportSerializer,
#     # TypeOfDamageSerializer, ValidateDamageReportSerializer
# )
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework import status
from django.utils.translation import ugettext_lazy as _


# class CreateDamageReportView(CreateAPIView):
#     serializer_class = CreateDamageReportSerializer
#     queryset = DamageReport.objects.all()


# class ListTypeOfDamagesView(ListAPIView):
#     serializer_class = TypeOfDamageSerializer
#     queryset = TypeOfDamage.objects.all()


# class RetrieveDamageReportView(APIView):
#     def post(self, request):
#         serializer = ValidateDamageReportSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             try:
#                 damage_report = DamageReport.objects.get(
#                     billing_id=serializer.data['billing_id'],
#                     unique_id=serializer.data['unique_id']
#                 )
#             except DamageReport.DoesNotExist:
#                 return Response({
#                     'message': _('There is not damage report with given data.')
#                 },
#                     status=status.HTTP_404_NOT_FOUND
#                 )
#             return Response(
#                 RetrieveDamageReportSerializer(damage_report).data
#             )
