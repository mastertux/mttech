from django import forms
from advogados.models import Advogados

class AdvogadosForm(forms.ModelForm):
    class Meta:
        model = Advogados
        fields = ['nome','email','cpf', 'telefone']