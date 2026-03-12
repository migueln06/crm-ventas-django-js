from django.shortcuts import render

from rest_framework import generics
from .models import Prospecto
from .serializers import ProspectoSerializer

# Create your views here.
class ProspectoListAPI(generics.ListCreateAPIView):
    queryset = Prospecto.objects.all()
    serializer_class = ProspectoSerializer

class ProspectoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prospecto.objects.all()
    serializer_class = ProspectoSerializer