from django.shortcuts import render
from .forms import PersonaForm


def home(request):
    return render(request, 'clasificador/index.html')


def clasificar(persona):
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
            persona.categoria = clasificar(persona)
            persona.save()
            return render(request, 'clasificador/resultado.html', {'persona': persona})
    else:
        form = PersonaForm()
    return render(request, 'clasificador/formulario.html', {'form': form})


def daisy(request):
    resultado = None
    error = None
    if request.method == 'POST':
        try:
            S = int(request.POST.get('puntaje', 0))
            p  = min(S // 1000, 100)
            S -= p * 1000
            gr = min(S // 100, 100 - p)
            S -= gr * 100
            go = min(S // 10, 100 - p - gr)
            S -= go * 10
            b = S
            if p + gr + go + b <= 100:
                resultado = {'Perfect': p, 'Great': gr, 'Good': go, 'Bad': b}
            else:
                error = "NO SOLUTION"
        except ValueError:
            error = "Ingresa un número válido"
    return render(request, 'clasificador/daisy.html', {'resultado': resultado, 'error': error})


def birds(request):
    resultado = None
    error = None
    if request.method == 'POST':
        try:
            arr = list(map(int, request.POST.get('avistamientos', '').split()))
            if not arr or any(b not in range(1, 6) for b in arr):
                error = "Solo se permiten valores entre 1 y 5"
            else:
                freq = [0] * 6
                for b in arr:
                    freq[b] += 1
                resultado = max(range(1, 6), key=lambda x: freq[x])
        except ValueError:
            error = "Ingresa números válidos separados por espacios"
    return render(request, 'clasificador/birds.html', {'resultado': resultado, 'error': error})