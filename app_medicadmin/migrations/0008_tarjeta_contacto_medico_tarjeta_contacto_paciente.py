# Generated by Django 4.1.3 on 2023-02-21 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_medicadmin', '0007_remove_paciente_tarjeta_de_contacto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarjeta_contacto',
            name='medico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_medicadmin.paciente'),
        ),
        migrations.AddField(
            model_name='tarjeta_contacto',
            name='paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_medicadmin.medico'),
        ),
    ]
