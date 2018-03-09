from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Permission
from advogados.models import Advogados
from core.models import User


class AdvogadosForm(forms.ModelForm):
    username = forms.CharField(label='Usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirmar senha', widget=forms.PasswordInput)
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(AdvogadosForm, self).__init__(*args, **kwargs)
        update_initial = {}

        if self.instance.id:
            self.fields['username'].widget.attrs['readonly'] = True
            self.fields['username'].required = False
            self.fields['password'].required = False
            self.fields['confirm_password'].required = False
        
            user = User.objects.get(advogado_id=self.instance.id)
            update_initial['username'] = user.username
            kwargs.update(initial=update_initial)
            super(AdvogadosForm, self).__init__(*args, **kwargs)
        
    

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).count() > 0 and self.instance.id is None:
            raise ValidationError('Username já esta sendo utilizado')
        return username


    def clean_password(self):
        password = self.data['password']
        confirm_password = self.data['confirm_password']

        if(password != confirm_password):
            raise ValidationError('Senhas não são iguais')
        return password


    def save(self, **kwargs):
        isNewUser = self.instance.id
        advogado = super(AdvogadosForm, self).save(**kwargs)
        if isNewUser is None:
            user = User()
            user.username = self.cleaned_data['username']
            user.set_password(self.cleaned_data['password'])
            user.advogado = advogado
            user.is_advogado = True
            user.save()

            permission = Permission.objects.filter(codename__in=['add_ordemservico','add_proposta'])
            user.user_permissions.add(permission.first())
            user.user_permissions.add(permission.last())
            
        else:
            user = User.objects.get(username=self.cleaned_data.get('username'))
            if self.cleaned_data.get('password') != "":
                user.set_password(self.cleaned_data.get('password'))
                user.save()
        return advogado


    class Meta:
        model = Advogados
        fields = ['nome','email','cpf', 'telefone']