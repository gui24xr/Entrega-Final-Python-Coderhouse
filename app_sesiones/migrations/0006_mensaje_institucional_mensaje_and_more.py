# Generated by Django 4.1.3 on 2023-02-24 02:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sesiones', '0005_mensaje_institucional_remove_novedades_autor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje_institucional',
            name='mensaje',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mensaje_institucional',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2023, 2, 23, 23, 35, 42, 793787), verbose_name='Fecha Anunciado'),
        ),
        migrations.AlterField(
            model_name='mensaje_institucional',
            name='horario',
            field=models.TimeField(default=datetime.datetime(2023, 2, 23, 23, 35, 42, 793787), verbose_name='Horario Anunciado'),
        ),
    ]