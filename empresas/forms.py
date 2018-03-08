from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Permission
from empresas.models import Empresas
from core.models import User

class EmpresasForm(forms.ModelForm):
    username = forms.CharField(label='Usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirmar senha', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(EmpresasForm, self).__init__(*args, **kwargs)
        update_initial = {}

        if self.instance.id:
            self.fields['username'].widget.attrs['readonly'] = True
            self.fields['username'].required = False
            self.fields['password'].required = False
            self.fields['confirm_password'].required = False
        
            user = User.objects.get(empresa_id=self.instance.id)
            update_initial['username'] = user.username
            kwargs.update(initial=update_initial)
            super(EmpresasForm, self).__init__(*args, **kwargs)
    

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
        empresa = super(EmpresasForm, self).save(**kwargs)
        if isNewUser is None:
            user = User()
            user.username = self.cleaned_data['username']
            user.set_password(self.cleaned_data['password'])
            user.empresa = empresa
            user.is_empresa = True
            user.save()

            permission = Permission.objects.get(codename='add_ordemservico')
            user.user_permissions.add(permission)

        else:
            user = User.objects.get(username=self.cleaned_data.get('username'))
            if self.cleaned_data.get('password') != "":
                user.set_password(self.cleaned_data.get('password'))
                user.save()
        return empresa
    
    
    class Meta:
        model = Empresas
        fields = ['nome','ramo_atividade']