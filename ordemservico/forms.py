from django import forms
from ordemservico.models import OrdemServico, Proposta

class OrdemServicoForm(forms.ModelForm):
    
    descricao = forms.CharField(widget=forms.TextInput())
    class Meta:
        model = OrdemServico
        fields = ['titulo','descricao']

class PropostaForm(forms.ModelForm):
    class Meta:
        model = Proposta
        fields = ['valor']