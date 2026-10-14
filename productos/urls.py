# pruductoss/urls.py
"""URLs de la app pruductoss — W02."""
from django.urls import path
from . import views

app_name = 'pruductoss'

urlpatterns = [
    path('', views.index, name='inicio'),
    # Espiral 2 W05:
    # path('lista/',          views.pruductosListView.as_view(),   name='lista'),
    # path('nuevo/',          views.pruductosCreateView.as_view(), name='crear'),
    # path('<int:pk>/',       views.pruductosDetailView.as_view(), name='detalle'),
    # path('<int:pk>/editar/',views.pruductosUpdateView.as_view(), name='editar'),
]