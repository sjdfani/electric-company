# Generated by Django 3.2.15 on 2022-09-05 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('damage', '0005_alter_damagereport_date_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='damagereport',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='damagereport',
            name='date_time',
        ),
        migrations.AddField(
            model_name='damagereport',
            name='created_datetime',
            field=models.DateTimeField(auto_now_add=True, default=None, verbose_name='Created datetime'),
            preserve_default=False,
        ),
    ]