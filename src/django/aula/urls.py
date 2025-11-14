from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('bye/', views.bye),
    path('edad/<int:anios>/<int:futuro>/', views.edad),
    path('plantilla1/', views.primer_plantilla),
    path('plantilla2/', views.segunda_plantilla),
    path('plantilla3/', views.tercer_plantilla),
]