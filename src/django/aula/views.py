from django.http import HttpResponse
from datetime import date
from django.template import Template, Context 
from django.template.loader import get_template
from django.shortcuts import render 

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