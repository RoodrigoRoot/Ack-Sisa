from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    AREA_JOB= [
                ('Preventa','Preventa'),
                ('Soporte','Sopote'),
                ('Administración','Administración'),
                ('Implementación','Implementación'),
                ('Ventas','Ventas'),
                ('Compras','Compras'),
                ]
    POSITION_JOB = [
                ('ING','Ingeniero'),
                ('Ejecutivo','Ejecutivo'),
                ('Administrativo','Administrativo'),
                   ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    area =  models.CharField(("Área"),choices=AREA_JOB,max_length=15) 
    position = models.CharField(("Posición"),choices=POSITION_JOB,max_length=15) 

    def __str__(self):
        return "{} {} de {}".format(self.user.username,self.position,self.area)
