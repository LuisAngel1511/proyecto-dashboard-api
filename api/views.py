# api/views.py

import os
import pandas as pd
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response

# 1. Define la ruta exacta a tu archivo CSV
FILE_PATH = os.path.join(settings.BASE_DIR, 'api', 'dataset.csv')

class CalidadDatosView(APIView):
    """
    Esta es la vista que manejará las peticiones a nuestra API.
    """
    def get(self, request, *args, **kwargs):
        
        # 2. Intenta leer el archivo CSV con Pandas
        try:
            df = pd.read_csv(FILE_PATH)
        except FileNotFoundError:
            return Response({"error": "No se encontró el archivo dataset.csv"}, status=404)
        except Exception as e:
            return Response({"error": f"Error al leer el archivo: {str(e)}"}, status=500)

        # 3. Realizar todos los cálculos (el núcleo de tu proyecto)
        
        # Resumen general
        resumen_filas, resumen_cols = df.shape
        
        # Cálculo de Nulos
        nulos_data = df.isnull().sum()
        nulos_columnas = nulos_data.index.tolist()
        nulos_conteo = nulos_data.values.tolist()

        # Cálculo de Duplicados
        total_duplicados = int(df.duplicated().sum())
        total_unicos = len(df) - total_duplicados

        # Cálculo de Tipos de Datos
        # (Convertimos los tipos de Pandas a strings simples para el JSON)
        tipos_data = df.dtypes.astype(str).value_counts()
        tipos_etiquetas = tipos_data.index.tolist()
        tipos_conteo = tipos_data.values.tolist()

        # 4. Construir el diccionario de respuesta
        # (Debe tener la misma estructura que tu 'calidad_datos.json' del frontend)
        response_data = {
            "resumen": {
                "total_filas": resumen_filas,
                "total_columnas": resumen_cols,
                "dataset_nombre": "dataset.csv" # Usamos el nombre real
            },
            "valores_nulos_por_columna": {
                "columnas": nulos_columnas,
                "conteo": nulos_conteo
            },
            "conteo_duplicados": {
                "etiquetas": ["Filas Únicas", "Filas Duplicadas"],
                "conteo": [total_unicos, total_duplicados]
            },
            "distribucion_tipos_datos": {
                "etiquetas": tipos_etiquetas,
                "conteo": tipos_conteo
            }
        }
        
        # 5. Enviar la respuesta como JSON
        return Response(response_data)