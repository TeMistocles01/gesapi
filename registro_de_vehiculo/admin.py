from django.contrib import admin

# Register your models here.
from .models import Registro_Conductor

class Registro_ConductorAdmin(admin.ModelAdmin):
    
    
    
    list_display = ('Placa','Password')
    list_filter = ('Placa','Password') 



admin.site.register(Registro_Conductor,Registro_ConductorAdmin)
