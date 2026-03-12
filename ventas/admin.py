from django.contrib import admin
from .models import Prospecto, Venta

# Register your models here.


@admin.register(Prospecto)
class ProspectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'origen', 'estado', 'fecha_creacion', 'asignado_a')
    list_filter = ('estado', 'origen')
    search_fields = ('nombre', 'email')

admin.site.register(Venta)