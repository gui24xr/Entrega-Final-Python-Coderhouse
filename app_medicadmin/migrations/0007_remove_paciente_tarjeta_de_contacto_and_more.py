# Generated by Django 4.1.3 on 2023-02-21 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_medicadmin', '0006_tarjeta_obra_social_num_afiliado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='tarjeta_de_contacto',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='tarjeta_obra_social',
        ),
        migrations.AddField(
            model_name='tarjeta_obra_social',
            name='paciente',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_medicadmin.paciente'),
        ),
    ]
