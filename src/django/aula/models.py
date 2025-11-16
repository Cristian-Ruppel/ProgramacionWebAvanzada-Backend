from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Persona(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    edad = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Musico(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    instrumento = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.instrumento})"

class Album(models.Model):
    nombre = models.CharField(max_length=200)
    artista = models.ForeignKey(Musico, on_delete=models.CASCADE)
    release_date = models.DateField()
    estrellas = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.artista.first_name} {self.artista.last_name} ({self.estrellas} estrellas)"