from django.shortcuts import render, redirect
from .forms import AsociadoForm

def registrar_asociado(request):
    if request.method == 'POST':
        form = AsociadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro_exitoso')
    else:
        form = AsociadoForm()

    return render(request, 'asociados/registro.html', {'form': form})


def registro_exitoso(request):
    return render(request, 'asociados/exito.html')
