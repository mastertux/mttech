from django import forms
from ordemservico.models import OrdemServico

class OrdemServicoForm(forms.ModelForm):
    class Meta:
        model = OrdemServico
        fields = ['titulo','empresa','descricao']