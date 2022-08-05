from django.urls import path
from .views import RegisterUser, RegisterOperator, Login

app_name = 'users'

urlpatterns = [
    path('register-user/', RegisterUser.as_view(), name='register-user'),
    path('register-operator/', RegisterOperator.as_view(),
         name='register-operator'),
    path('login/', Login.as_view(), name='login'),
]
