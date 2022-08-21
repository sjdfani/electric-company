from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext_lazy as _


class Suggestion(models.Model):
    full_name = models.CharField(max_length=200, verbose_name=_('Full name'))
    email = models.EmailField(verbose_name=_('Email'))
    phone_number = PhoneNumberField(verbose_name=_('Phone number'))
    description = models.TextField(verbose_name=_('Description'))

    def __str__(self) -> str:
        return self.phone_number
