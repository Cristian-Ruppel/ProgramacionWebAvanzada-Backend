from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('bye/', views.bye),
    path('edad/<int:anios>/<int:futuro>/', views.edad),
]