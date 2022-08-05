from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from .serializer import RegisterUserSerializer, RegisterOperatorSerializer
from .models import User
from .permissions import IsSuperuser


class RegisterUser(CreateAPIView):
    serializer_class = RegisterUserSerializer
    queryset = User.objects.all()


class RegisterOperator(CreateAPIView):
    permission_classes = [IsSuperuser]
    serializer_class = RegisterOperatorSerializer
    queryset = User.objects.all()
