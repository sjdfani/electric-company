from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid
from users.models import User


class Status(models.IntegerChoices):
    TODO = (1, _('TODO'))
    IN_PROGRESS = (2, _('In progress'))
    DONE = (3, _('Done'))
    FAILURE = (4, _('Failure'))
    LACK_OF_SUFFICIENT_INFORMATION = (5, _('Lack of sufficient information'))


def uuid_hex():
    return uuid.uuid4().hex


class TypeOfDamage(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Type of damage'))

    def __str__(self):
        return self.title


class DamageReport(models.Model):
    unique_id = models.CharField(
        default=uuid_hex, max_length=500, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='user_damage_reports', verbose_name=_('User'))
    billing_id = models.CharField(max_length=100, verbose_name=_('Billing ID'))
    last_bill_image = models.FileField(
        upload_to='images/', verbose_name=_('Last bill image'), blank=True, null=True)
    national_card_image = models.FileField(
        upload_to='images/', verbose_name=_('National card image'), blank=True, null=True)
    ownership_doc_image = models.FileField(
        upload_to='images/', verbose_name=_('Ownership document image'), blank=True, null=True)
    created_datetime = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Created datetime'))
    type_of_damage = models.ForeignKey(
        TypeOfDamage, on_delete=models.SET_NULL, related_name='type_damage_reports',
        blank=True, null=True, verbose_name=_('Type of damage')
    )
    description = models.TextField(verbose_name=_('Description'))
    amount_of_damages = models.FloatField(verbose_name=_('Amount of damages'))
    status = models.IntegerField(
        choices=Status.choices, default=Status.TODO, verbose_name=_('Status'))
    operator = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        related_name='damage_reports_operator', verbose_name=_('Operator'), blank=True, null=True
    )
    done_date = models.DateTimeField(
        verbose_name=_('done at'), blank=True, null=True)
    operator_description = models.TextField(verbose_name=_(
        'Operator_Description'), blank=True, null=True)


class AdditionalDocument(models.Model):
    image = models.FileField(
        upload_to='images/', verbose_name=_('Image'), blank=True, null=True)
    damage_report = models.ForeignKey(
        DamageReport, on_delete=models.CASCADE, related_name='additional_documents', verbose_name=_('Damage report')
    )
