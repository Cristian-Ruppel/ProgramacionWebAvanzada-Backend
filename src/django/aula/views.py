from django.http import HttpResponse
from datetime import date

def hello(request):
    return HttpResponse("Hola mundo desde mi primera vista en Django!")

def bye(request):
    return HttpResponse("Hasta luego")

def edad(request, anios, futuro):
    incremento = futuro - date.today().year
    cumplira = anios + incremento
    mensaje = "En el año %d cumplirás %d años"%(futuro, cumplira)
    return HttpResponse(mensaje)