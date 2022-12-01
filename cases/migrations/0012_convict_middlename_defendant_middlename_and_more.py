# Generated by Django 4.1.1 on 2022-12-01 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0011_convict_charges'),
    ]

    operations = [
        migrations.AddField(
            model_name='convict',
            name='middleName',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Middle Name'),
        ),
        migrations.AddField(
            model_name='defendant',
            name='middleName',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Middle Name'),
        ),
        migrations.AddField(
            model_name='judge',
            name='middleName',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Middle Name'),
        ),
    ]
