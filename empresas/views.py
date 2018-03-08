from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from empresas.models import Empresas
from empresas.forms import EmpresasForm


class EmpresasList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = '/login'
    permission_required = 'empresas.add_empresas'
    model = Empresas

class EmpresasCreate(LoginRequiredMixin, CreateView):
    login_url = '/login'
    success_url = reverse_lazy('empresas_list')
    form_class = EmpresasForm
    template_name = 'empresas/empresas_form.html'

    def get_form_kwargs(self):
        kw = super(EmpresasCreate, self).get_form_kwargs()
        kw['request'] = self.request
        return kw

class EmpresasUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = '/login'
    permission_required = 'empresas.change_empresas'
    model = Empresas
    form_class = EmpresasForm
    success_url = reverse_lazy('empresas_list')

    def get_form_kwargs(self):
        kw = super(EmpresasUpdate, self).get_form_kwargs()
        kw['request'] = self.request
        return kw

class EmpresasDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url = '/login'
    permission_required = 'empresas.delete_empresas'
    model = Empresas
    success_url = reverse_lazy('empresas_list')
