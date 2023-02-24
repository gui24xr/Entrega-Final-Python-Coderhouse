from django.contrib import admin
from .models import*
# Register your models here.

admin.site.register(paciente)
admin.site.register(medico)
admin.site.register(turno)
admin.site.register(tarjeta_contacto)
admin.site.register(tarjeta_obra_social)
admin.site.register(aviso_llegada)
admin.site.register(post_novedad)