from django.db import models

# Create your models here.
class Registro_Conductor(models.Model):
    
    Placa = models.CharField('Placa:',max_length=255,blank=False, null=False, unique=True,primary_key=True)
    Password = models.CharField('Contraseña:',max_length=100,blank=False, null=False)
   
    class Meta:
        verbose_name='Registro de conductor'
        verbose_name_plural='Registro de conductor'
        # funcion para convertir texto ingresado por teclado en minuscula en mayuscula

   
    

    def __str__(self):
         return 'Placa: %s Contraseña: %s '%(self.Placa,self.Password)
