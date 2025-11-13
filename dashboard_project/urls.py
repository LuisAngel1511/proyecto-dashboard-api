# dashboard_project/urls.py
from django.contrib import admin
from django.urls import path, include  # <--- ¡IMPORTANTE: añade include aquí!

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Aquí conectamos tu app:
    # Cualquier ruta que empiece con 'api/' se enviará a api/urls.py
    path('api/', include('api.urls')), 
]   