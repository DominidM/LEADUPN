from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        exclude = ['categoria']
        labels = {
            'nombre': 'Nombre',
            'edad': 'Edad',
            'ingresos': 'Ingresos mensuales (S/)',
            'deudas': 'Deudas totales (S/)',
            'tiene_empleo': '¿Tiene empleo?',
            'condicion_salud': 'Condición de salud',
        }