# Generated by Django 4.1.3 on 2023-02-24 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sesiones', '0007_alter_mensaje_institucional_fecha_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje_institucional',
            name='autor',
            field=models.CharField(default=3, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mensaje_institucional',
            name='fecha',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha Anunciado'),
        ),
        migrations.AlterField(
            model_name='mensaje_institucional',
            name='horario',
            field=models.TimeField(auto_now_add=True, verbose_name='Horario Anunciado'),
        ),
        migrations.AlterField(
            model_name='perfil_usuario',
            name='foto_perfil',
            field=models.ImageField(blank=True, default='avatares/med1.jpg', null=True, upload_to='avatares'),
        ),
    ]
