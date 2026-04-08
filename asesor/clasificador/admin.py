from django.contrib import admin
from .models import Persona

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display  = ['nombre', 'edad', 'ingresos', 'deudas', 'tiene_empleo', 'condicion_salud', 'categoria']
    list_filter   = ['categoria', 'condicion_salud', 'tiene_empleo']
    search_fields = ['nombre', 'categoria']
    ordering      = ['-id']