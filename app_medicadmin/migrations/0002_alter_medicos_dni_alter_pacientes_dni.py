# Generated by Django 4.1.3 on 2023-02-13 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_medicadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicos',
            name='dni',
            field=models.IntegerField(max_length=8),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='dni',
            field=models.IntegerField(max_length=8),
        ),
    ]
