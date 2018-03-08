from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from advogados.models import Advogados
from advogados.forms import AdvogadosForm

class AdvogadosList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = '/login'
    permission_required = 'advogados.add_advogados'
    model = Advogados

class AdvogadosCreate(LoginRequiredMixin, CreateView):
    login_url = '/login'
    success_url = reverse_lazy('advogados_list')
    form_class = AdvogadosForm
    template_name = 'advogados/advogados_form.html'

    def get_form_kwargs(self):
        kw = super(AdvogadosCreate, self).get_form_kwargs()
        kw['request'] = self.request
        return kw

class AdvogadosUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = '/login'
    permission_required = 'advogados.change_advogados'
    model = Advogados
    form_class = AdvogadosForm
    success_url = reverse_lazy('advogados_list')

    def get_form_kwargs(self):
        kw = super(AdvogadosUpdate, self).get_form_kwargs()
        kw['request'] = self.request
        return kw

class AdvogadosDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url = '/login'
    permission_required = 'advogados.delete_advogados'
    model = Advogados
    success_url = reverse_lazy('advogados_list')
