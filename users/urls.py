from django.urls import path
from .views import RegisterUser,RegisterOperator

app_name = 'users'

urlpatterns = [
    path('register-user/', RegisterUser.as_view(), name='register-user'),
    path('register-operator/', RegisterOperator.as_view(), name='register-operator'),
]
