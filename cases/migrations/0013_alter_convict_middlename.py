# Generated by Django 4.1.1 on 2022-12-01 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0012_convict_middlename_defendant_middlename_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convict',
            name='middleName',
            field=models.CharField(default=' ', max_length=32, verbose_name='Middle Name'),
        ),
    ]
