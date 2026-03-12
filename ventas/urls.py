from django.urls import path
from .views import ProspectoListAPI, ProspectoDetailAPI # <--- Importa la nueva vista



urlpatterns = [
    path('api/prospectos/', ProspectoListAPI.as_view(), name='prospecto-list'),
    # Esta ruta usa el ID (pk) para saber cuál borrar
    path('api/prospectos/<int:pk>/', ProspectoDetailAPI.as_view(), name='prospecto-detail'),
]