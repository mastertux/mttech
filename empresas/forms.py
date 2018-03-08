from django import forms
from empresas.models import Empresas

class EmpresasForm(forms.ModelForm):
    class Meta:
        model = Empresas
        fields = ['nome','ramo_atividade']