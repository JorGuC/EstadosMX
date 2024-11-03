from django.urls import path
from .views import index, cargar_municipios

urlpatterns = [
    path('', index, name='index'),
    path('cargar-municipios/', cargar_municipios, name='cargar_municipios'),
]
