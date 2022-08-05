from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext_lazy as _
from .manager import UserManager


class User(AbstractUser):
    full_name = models.CharField(
        max_length=200, verbose_name=_('Full name'), null=True)
    phone_number = PhoneNumberField(
        unique=True, verbose_name=_('Phone number'))
    national_code = models.CharField(
        max_length=10, verbose_name=_('National code'))
    province = models.CharField(max_length=200, verbose_name=_('Province'))
    city = models.CharField(max_length=200, verbose_name=_('City'))
    postal_code = models.CharField(
        max_length=100, verbose_name=_('Postal code'))
    address = models.TextField(verbose_name=_('Address'))
    api_key = models.CharField(max_length=200, verbose_name=_(
        'API key'), blank=True, null=True)
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['full_name']
    username = None
    first_name = None
    last_name = None
    objects = UserManager()

    def __str__(self):
        return str(self.phone_number)
