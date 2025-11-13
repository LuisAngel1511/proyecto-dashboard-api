# api/urls.py
from django.urls import path
from .views import CalidadDatosView

urlpatterns = [
    # Esta es la ruta específica: http://.../api/calidad-datos/
    path('calidad-datos/', CalidadDatosView.as_view(), name='calidad_datos'),
]