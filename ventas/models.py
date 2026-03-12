from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Prospecto(models.Model):
    # Opciones de origen para análisis posterior
    ORIGEN_CHOICES = [
        ('IG', 'Instagram'),
        ('TK', 'TikTok'),
        ('WB', 'Web'),
        ('RE', 'Referido'),
    ]
    
    # Opciones de estado del embudo de ventas
    ESTADO_CHOICES = [
        ('NUEVO', 'Nuevo'),
        ('CONTACTADO', 'Contactado'),
        ('CALIFICADO', 'Calificado'),
        ('PERDIDO', 'Perdido'),
        ('CERRADO', 'Venta Cerrada'),
    ]

    nombre = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True)
    origen = models.CharField(max_length=2, choices=ORIGEN_CHOICES, default='WB')
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES, default='NUEVO')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    notas = models.TextField(blank=True)
    asignado_a = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.get_estado_display()}"

class Venta(models.Model):
    prospecto = models.OneToOneField(Prospecto, on_delete=models.CASCADE, related_name='venta')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    metodo_pago = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"Venta #{self.id} - {self.prospecto.nombre} (${self.monto})"