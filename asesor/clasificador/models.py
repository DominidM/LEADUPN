from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    ingresos = models.FloatField()
    deudas = models.FloatField()
    tiene_empleo = models.BooleanField()
    condicion_salud = models.CharField(max_length=50, choices=[
        ('buena', 'Buena'),
        ('regular', 'Regular'),
        ('mala', 'Mala'),
    ])
    categoria = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nombre