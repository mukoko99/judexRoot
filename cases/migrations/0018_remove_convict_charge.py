# Generated by Django 4.1.1 on 2022-12-01 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0017_alter_convict_charge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='convict',
            name='charge',
        ),
    ]
