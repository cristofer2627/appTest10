from django.db import models

class Preguntas(models.Model):
    preguntas_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Opcion(models.Model):
    preguntas = models.ForeignKey(Preguntas, on_delete=models.CASCADE)
    opcion_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
