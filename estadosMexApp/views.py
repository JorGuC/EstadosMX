from django.http import JsonResponse
from .models import Municipio
from django.shortcuts import render
from .models import Estado

def cargar_municipios(request):
    estado_id = request.GET.get('estado_id')
    municipios = Municipio.objects.filter(estado_id=estado_id).values('id', 'nombre')
    return JsonResponse(list(municipios), safe=False)

def index(request):
    estados = Estado.objects.all()
    return render(request, 'estadosMexApp/index.html', {'estados': estados})