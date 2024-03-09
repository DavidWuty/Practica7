from django.contrib import admin
from .models import Juego
# Register your models here.

class JuegoAdmin(admin.ModelAdmin):
    readonly_fields=("fecha_creacion",)

admin.site.register(Juego,JuegoAdmin)