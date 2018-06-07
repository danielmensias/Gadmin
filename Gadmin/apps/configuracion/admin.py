from django.contrib import admin
from .models import Raza, TipoRodeo, Vacuna, Tecnico

# Register your models here.
admin.site.register(Raza)
admin.site.register(TipoRodeo)
admin.site.register(Vacuna)
admin.site.register(Tecnico)