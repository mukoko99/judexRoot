# Generated by Django 4.1.1 on 2022-12-02 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0017_rename_convict_convictions_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Convictions',
            new_name='Conviction',
        ),
    ]
