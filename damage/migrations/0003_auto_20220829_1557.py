# Generated by Django 3.2.15 on 2022-08-29 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('damage', '0002_auto_20220821_1327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='damagereport',
            name='date',
        ),
        migrations.RemoveField(
            model_name='damagereport',
            name='time',
        ),
        migrations.AddField(
            model_name='damagereport',
            name='date_time',
            field=models.DateTimeField(default=None, verbose_name='Date-Time'),
            preserve_default=False,
        ),
    ]
