# Generated by Django 4.1.1 on 2022-11-07 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0002_alter_case_defendant_alter_case_judge'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='region',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Case Region'),
        ),
        migrations.AddField(
            model_name='defendant',
            name='region',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Defendant Region'),
        ),
        migrations.AddField(
            model_name='defendantgroup',
            name='region',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Defendant Group Region'),
        ),
        migrations.AddField(
            model_name='judge',
            name='region',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Judge Region'),
        ),
        migrations.AddField(
            model_name='judgegroup',
            name='region',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Judge Group Region'),
        ),
    ]
