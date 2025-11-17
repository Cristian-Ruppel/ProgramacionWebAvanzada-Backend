from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('bye/', views.bye),
    path('edad/<int:anios>/<int:futuro>/', views.edad),
    path('plantilla1/', views.primer_plantilla),
    path('plantilla2/', views.segunda_plantilla),
    path('plantilla3/', views.tercer_plantilla),
    path('alumnos/', views.mostrar_alumnos, name='mostrar_alumnos'),
    path('crear_musico/<str:nombre>/<str:apellido>/<str:instrumento>/', views.crear_musico, name='crear_musico'),
    path('crear_album/<str:nombre>/<int:estrellas>/<int:artista_id>/', views.crear_album, name='crear_album'),
    path('api_first/', views.api_first, name='api_first'),
]