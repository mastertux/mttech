from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from ordemservico.models import OrdemServico
from ordemservico.forms import OrdemServicoForm


class OrdemServicoList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = '/login'
    permission_required = 'ordemservico.add_ordemservico'
    model = OrdemServico

class OrdemServicoCreate(LoginRequiredMixin, CreateView):
    login_url = '/login'
    success_url = reverse_lazy('ordemservico_list')
    form_class = OrdemServicoForm
    template_name = 'ordemservico/ordemservico_form.html'

class OrdemServicoUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = '/login'
    permission_required = 'ordemservico.change_ordemservico'
    model = OrdemServico
    form_class = OrdemServicoForm
    success_url = reverse_lazy('ordemservico_list')

class OrdemServicoDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url = '/login'
    permission_required = 'ordemservico.delete_ordemservico'
    model = OrdemServico
    success_url = reverse_lazy('ordemservico_list')
