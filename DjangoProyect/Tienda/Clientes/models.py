from django.db import models

class Preguntas(models.Model):
    preguntas_text = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')

class Opcion(models.Model):
    preguntas = models.ForeignKey(Preguntas, on_delete=models.CASCADE)
    opcion_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Users(models.Model):
    user_name = models.CharField(max_length=500)
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)