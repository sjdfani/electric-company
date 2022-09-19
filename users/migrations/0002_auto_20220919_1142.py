# Generated by Django 3.2.15 on 2022-09-19 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='account_number',
            field=models.CharField(default=None, max_length=20, verbose_name='Account number'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='card_number',
            field=models.CharField(default=None, max_length=16, verbose_name='Card number'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='shaba_number',
            field=models.CharField(default=None, max_length=16, verbose_name='Shaba number'),
            preserve_default=False,
        ),
    ]
