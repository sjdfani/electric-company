from django.db import models
from django.utils.translation import ugettext_lazy as _
from users.models import User


class Suggestion(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_('Phone number'))
    description = models.TextField(verbose_name=_('Description'))

    def __str__(self) -> str:
        return str(self.user.phone_number)
