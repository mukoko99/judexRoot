# Generated by Django 4.1.1 on 2022-12-02 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0018_rename_convictions_conviction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defendant',
            name='middleName',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Middle Initial'),
        ),
    ]
