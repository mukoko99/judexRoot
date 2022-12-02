# Generated by Django 4.1.1 on 2022-12-02 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0014_alter_defendant_middlename_alter_judge_middlename'),
    ]

    operations = [
        migrations.AddField(
            model_name='convict',
            name='sentenceEnd',
            field=models.DateField(blank=True, null=True, verbose_name='Date Sentencing Ends'),
        ),
        migrations.AddField(
            model_name='convict',
            name='sentenceStart',
            field=models.DateField(blank=True, null=True, verbose_name='Date Sentencing Starts'),
        ),
    ]