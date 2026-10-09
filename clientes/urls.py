# cliente/urls.py
"""URLs de la app cliente — W01 (mínimo funcional)."""
from django.urls import path
from django.http import HttpResponse

app_name = 'cliente'


def bienvenida_cliente(request):
    """Vista temporal de bienvenida para la app cliente."""
    return HttpResponse(
        "<h2>📦 Módulo Cliente</h2>"
        "<p>En construcción — Espiral 2 (W04)</p>",
        content_type='text/html; charset=utf-8'
    )


urlpatterns = [
    path('', bienvenida_cliente, name='inicio'),
]
