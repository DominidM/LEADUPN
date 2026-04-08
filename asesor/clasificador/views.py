from django.shortcuts import render
from .forms import PersonaForm
from .models import Persona


def clasificar_persona(persona):
    ratio_deuda = persona.deudas / persona.ingresos if persona.ingresos > 0 else 999
    if ratio_deuda > 0.5:
        return "Riesgo Crédito"
    elif persona.condicion_salud in ['regular', 'mala']:
        return "Riesgo Salud"
    elif not persona.tiene_empleo:
        return "Riesgo Laboral"
    else:
        return "Supply Chain - Salida de Pedidos"


def formulario(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            persona = form.save(commit=False)
            persona.categoria = clasificar_persona(persona)
            persona.save()
            return render(request, 'clasificador/resultado.html', {'persona': persona})
    else:
        form = PersonaForm()
    return render(request, 'clasificador/formulario.html', {'form': form})


def lista(request):
    personas = Persona.objects.all().order_by('-id')
    return render(request, 'clasificador/lista.html', {'personas': personas})