# Generated by Django 4.1.1 on 2022-12-01 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0016_alter_convict_charge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convict',
            name='charge',
            field=models.ManyToManyField(to='cases.charge'),
        ),
    ]
