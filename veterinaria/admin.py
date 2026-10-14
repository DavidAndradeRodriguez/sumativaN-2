from django.contrib import admin
from .models import Cliente, Atencion

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre','rut','monto')
@admin.register(Atencion)
class AtencionAdmin(admin.ModelAdmin):
    list_display = ('nombre','raza','edad','dueño')