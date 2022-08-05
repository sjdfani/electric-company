from django.urls import path
from .views import (
    RegisterUser, RegisterOperator, Login,
    ForgotPassword, VerifyForgotPassword, ConfirmForgotPassword
)

app_name = 'users'

urlpatterns = [
    path('register-user/', RegisterUser.as_view()),
    path('register-operator/', RegisterOperator.as_view()),
    path('login/', Login.as_view()),
    path('forgot-password/', ForgotPassword.as_view()),
    path('verify-forgot-password/', VerifyForgotPassword.as_view()),
    path('confirm-forgot-password/', ConfirmForgotPassword.as_view()),
]
