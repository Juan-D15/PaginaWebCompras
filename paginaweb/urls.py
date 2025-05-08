from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('asociados/', include('asociados.urls')),
    path('', lambda request: redirect('registrar_asociado')),  # Redirigir "/" al formulario
]
