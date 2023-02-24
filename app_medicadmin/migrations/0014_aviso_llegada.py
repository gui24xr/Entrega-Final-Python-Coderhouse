# Generated by Django 4.1.3 on 2023-02-23 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_medicadmin', '0013_delete_numero_telefonico_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='aviso_llegada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha Anunciado')),
                ('horario', models.TimeField(verbose_name='Horario Anunciado')),
                ('medico', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_medicadmin.medico')),
                ('paciente', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_medicadmin.paciente')),
            ],
        ),
    ]
