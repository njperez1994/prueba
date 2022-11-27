from django.contrib import admin

# Register your models here.
from . import  models
#registrando modelo en admin de django
@admin.register(models.viaje)

#creando clase que representa al modelo creado
class viajeAdmin(admin.ModelAdmin):
    #se ponen todas las entradas del modelo para que se puedan visulizar en el admin de django
    list_display = ('tipo','clase','cantidad','desde','hasta','fechasalida','fecharegreso')

    #se selecciona una entrada para que sirba de criterio de busqueda
    search_fields = ('tipo',)