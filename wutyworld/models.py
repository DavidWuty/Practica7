from django.db import models
from django.contrib.auth.models import User
# Create your models here.

OPCIONES_IDIOMA= [
    ('es', 'Español'),
    ('en', 'Ingles'),
    ('de', 'Aleman'),
    ('fr', 'Frances'),
]

class Juego(models.Model):
    titulo=models.CharField(max_length=300)
    idioma=models.CharField(max_length=15, choices=OPCIONES_IDIOMA)
    edad=models.IntegerField()
    principales=models.IntegerField()
    secundarios=models.IntegerField()
    fecha_creacion=models.DateTimeField(auto_now_add=True)
    usuario=models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.titulo}--{self.principales} principales,{self.secundarios} secundarios '