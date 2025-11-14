from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hola mundo desde mi primera vista en Django!")
