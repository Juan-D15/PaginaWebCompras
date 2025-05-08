from django import forms
from .models import Asociado

class AsociadoForm(forms.ModelForm):
    class Meta:
        model = Asociado
        fields = ['numero_cuenta', 'nombre', 'saldo', 'pin']
