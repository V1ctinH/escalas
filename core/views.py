from django.shortcuts import render
from core.models import Evento

def escalas(request):
    eventos = Evento.objects.all()
    return render(request, 'escalas.html', {'eventos': eventos})