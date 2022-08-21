from rest_framework.permissions import BasePermission
from users.models import User
from django.utils.translation import ugettext_lazy as _
from rest_framework.exceptions import APIException
from rest_framework import status


class CustomException(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _('API key is missing or invalid.')


class APIKeyPermission(BasePermission):

    def has_permission(self, request, view):
        api_key = request.META.get('HTTP_X_API_KEY')
        authorized = True
        if not api_key or api_key not in User.objects.all().values_list('api_key', flat=True):
            authorized = False
        if not authorized:
            raise CustomException()
        return True
