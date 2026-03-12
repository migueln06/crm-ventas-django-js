from rest_framework import serializers
from .models import Prospecto

class ProspectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prospecto
        fields = '__all__' # Esto incluirá todos los campos del modelo en el JSON
        