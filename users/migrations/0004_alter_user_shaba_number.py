# Generated by Django 3.2.15 on 2022-09-19 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220919_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='shaba_number',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Shaba number'),
        ),
    ]
