# Generated by Django 4.1.1 on 2022-12-01 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0013_alter_convict_middlename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defendant',
            name='middleName',
            field=models.CharField(default=' ', max_length=32, verbose_name='Middle Name'),
        ),
        migrations.AlterField(
            model_name='judge',
            name='middleName',
            field=models.CharField(default=' ', max_length=32, verbose_name='Middle Name'),
        ),
    ]
