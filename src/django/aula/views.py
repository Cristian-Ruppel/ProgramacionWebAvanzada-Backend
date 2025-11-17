from django.http import HttpResponse, JsonResponse 
from datetime import date
from django.template import Template, Context 
from django.template.loader import get_template
from django.shortcuts import render 
from .models import Alumno, Musico, Album 
from django.views.decorators.csrf import csrf_exempt
import json


def hello(request):
    return HttpResponse("Hola mundo desde mi primera vista en Django!")

def bye(request):
    return HttpResponse("Hasta luego")

def edad(request, anios, futuro):
    incremento = futuro - date.today().year
    cumplira = anios + incremento
    mensaje = "En el año %d cumplirás %d años"%(futuro, cumplira)
    return HttpResponse(mensaje)

def primer_plantilla(request): 
    plantilla = """
    <html>
    <body>
    <h2>
    Hola, esta es mi primer plantilla!
    </h2>
    </body>
    </html>"""
    
    tpl = Template(plantilla)
    ctx = Context({
        'nombre': 'Usuario', 
    })
    
    mensaje = tpl.render(ctx)
    
    return HttpResponse(mensaje)
    
def segunda_plantilla(request):
    tpl = get_template('segunda_plantilla.html')
    
    contexto = {
        'nombre': 'Juan Gonzales',
        'fecha_actual': date.today(), 
    }
    
    mensaje = tpl.render(contexto)
    
    return HttpResponse(mensaje)

def tercer_plantilla(request):
    contexto = {
        'nombre': 'Juan Gomez',
        'fecha_actual': date.today(),
    }

    return render(request, "tercer_plantilla.html", contexto)

def mostrar_alumnos(request):
    alumnos = Alumno.objects.all()
    
    return render(request, 'alumnos.html', {'alumnos': alumnos})


def crear_musico(request, nombre, apellido, instrumento):
    musico = Musico(first_name=nombre, last_name=apellido, instrumento=instrumento)
    musico.save()
    return HttpResponse(f"Se creó el músico {musico.first_name} {musico.last_name} con id {musico.id}")

def crear_album(request, nombre, estrellas, artista_id):
    try:
        artista = Musico.objects.get(id=artista_id)
        
        album = Album(nombre=nombre, artista=artista, release_date=date.today(), estrellas=estrellas)
        album.save()
        
        return HttpResponse(f"Se creó el álbum {album.nombre} del artista {artista.last_name} con id {album.id}")
    except Musico.DoesNotExist:
        return HttpResponse(f"Error: No se encontró un músico con el ID {artista_id}")


@csrf_exempt # Decorador para permitir POST sin token (solo para pruebas)
def api_first(request):
    if request.method == "GET":
        # Si es GET, devolvemos el JSON fijo
        respuesta = {"nombre": "Cristian", "apellido": "Ruppel", "edad": 35}
        return JsonResponse(respuesta)
    
    elif request.method == "POST":
        # Si es POST, leemos el JSON que nos envían en el "body"
        data = json.loads(request.body)
        
        # Creamos una respuesta "eco" con los datos recibidos
        resp = {
            "mensaje": "Datos recibidos con éxito",
            "nombre_recibido": data.get("nombre"),
            "apellido_recibido": data.get("apellido"),
            "edad_recibida": data.get("edad"),
        }
        return JsonResponse(resp)
    
    else:
        return JsonResponse({"error": "Método no soportado"}, status=405)