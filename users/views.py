from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializer import (
    RegisterUserSerializer, RegisterOperatorSerializer, LoginSerializer,
    ForgotPasswordSerializer, VerifyForgotPasswordSerializer,
    ConfirmForgotPasswordSerializer, UserSerializer, UpdateInformationSerializer
)
from .models import User
from .permissions import IsSuperuser
from .utils import get_tokens_for_user


class RegisterUser(CreateAPIView):
    serializer_class = RegisterUserSerializer
    queryset = User.objects.all()


class RegisterOperator(CreateAPIView):
    permission_classes = [IsSuperuser]
    serializer_class = RegisterOperatorSerializer
    queryset = User.objects.all()


class Login(APIView):
    def post(self, request):
        serilaizer = LoginSerializer(
            data=request.data, context={'request': request}
        )
        if serilaizer.is_valid(raise_exception=True):
            phone_number = serilaizer.validated_data['phone_number']
            password = serilaizer.validated_data['password']
            user = User.objects.filter(phone_number=phone_number).first()
            if user:
                user_data = UserSerializer(user)
                if user.is_superuser:
                    if user.check_password(password):
                        message = {
                            'role': 'admin',
                            'user': user_data.data,
                            'tokens': get_tokens_for_user(user)
                        }
                        return Response(message, status=status.HTTP_200_OK)
                    else:
                        message = {
                            'message': 'شماره موبایل یا رمز عبور اشتباه است'
                        }
                        return Response(message, status=status.HTTP_400_BAD_REQUEST)
                elif user.is_staff and not user.is_superuser:
                    if user.check_password(password):
                        message = {
                            'role': 'operator',
                            'user': user_data.data,
                            'tokens': get_tokens_for_user(user)
                        }
                        return Response(message, status=status.HTTP_200_OK)
                    else:
                        message = {
                            'message': 'شماره موبایل یا رمز عبور اشتباه است'
                        }
                        return Response(message, status=status.HTTP_400_BAD_REQUEST)
                elif user.is_active and not (user.is_superuser and user.is_staff):
                    if user.check_password(password):
                        message = {
                            'role': 'user',
                            'user': user_data.data,
                            'tokens': get_tokens_for_user(user)
                        }
                        return Response(message, status=status.HTTP_200_OK)
                    else:
                        message = {
                            'message': 'شماره موبایل یا رمز عبور اشتباه است'
                        }
                        return Response(message, status=status.HTTP_400_BAD_REQUEST)
            else:
                message = {'message': 'کاربری با این شماره موبایل یافت نشد'}
                return Response(message, status=status.HTTP_404_NOT_FOUND)


class ForgotPassword(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK)


class VerifyForgotPassword(APIView):
    def post(self, request):
        serializer = VerifyForgotPasswordSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            state, message = serializer.save()
            if state:
                return Response(message, status=status.HTTP_200_OK)
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


class ConfirmForgotPassword(APIView):
    def post(self, request):
        serializer = ConfirmForgotPasswordSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateInformationUser(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserSerializer
        return UpdateInformationSerializer

    def get_queryset(self):
        return User.objects.filter(phone_number=self.request.user.phone_number)
