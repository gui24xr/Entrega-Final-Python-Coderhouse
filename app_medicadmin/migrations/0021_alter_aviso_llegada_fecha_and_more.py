# Generated by Django 4.1.3 on 2023-02-24 16:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_medicadmin', '0020_alter_aviso_llegada_fecha_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aviso_llegada',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2023, 2, 24, 13, 15, 43, 83830), verbose_name='Fecha Anunciado'),
        ),
        migrations.AlterField(
            model_name='aviso_llegada',
            name='horario',
            field=models.TimeField(default=datetime.datetime(2023, 2, 24, 13, 15, 43, 83830), verbose_name='Horario Anunciado'),
        ),
        migrations.AlterField(
            model_name='turno',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2023, 2, 24, 13, 15, 43, 83830), verbose_name='Fecha Turno'),
        ),
        migrations.AlterField(
            model_name='turno',
            name='horario',
            field=models.TimeField(default=datetime.datetime(2023, 2, 24, 13, 15, 43, 83830), verbose_name='Horario Turno'),
        ),
    ]