from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_asociado, name='registrar_asociado'),
    path('exito/', views.registro_exitoso, name='registro_exitoso'),
]
