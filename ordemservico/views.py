from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import View
from django.shortcuts import redirect
from ordemservico.models import OrdemServico, Proposta
from ordemservico.forms import OrdemServicoForm, PropostaForm


class OrdemServicoList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = '/login'
    permission_required = 'ordemservico.add_ordemservico'
    model = OrdemServico

    def get_queryset(self):
        if self.request.user.is_empresa:
            return OrdemServico.objects.filter(empresa=self.request.user.empresa)
        return OrdemServico.objects.all()


class OrdemServicoCreate(LoginRequiredMixin, CreateView):
    login_url = '/login'
    success_url = reverse_lazy('ordemservico_list')
    form_class = OrdemServicoForm
    template_name = 'ordemservico/ordemservico_form.html'

    def form_valid(self, form):
        ordemservico = form.save(commit=False)
        ordemservico.empresa = self.request.user.empresa
        return super(OrdemServicoCreate, self).form_valid(form)


class OrdemServicoUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = '/login'
    permission_required = 'ordemservico.change_ordemservico'
    model = OrdemServico
    form_class = OrdemServicoForm
    success_url = reverse_lazy('ordemservico_list')

    def form_valid(self, form):
        ordemservico = form.save(commit=False)
        ordemservico.empresa = self.request.user.empresa
        return super(OrdemServicoUpdate, self).form_valid(form)


class OrdemServicoDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url = '/login'
    permission_required = 'ordemservico.delete_ordemservico'
    model = OrdemServico
    success_url = reverse_lazy('ordemservico_list')


class PropostaCreate(LoginRequiredMixin, CreateView):
    login_url = '/login'
    success_url = reverse_lazy('ordemservico_list')
    form_class = PropostaForm
    template_name = 'proposta/proposta_form.html'
    permission_required = 'proposta.add_proposta'

    
    def get(self, request, *args, **kwargs):
        request.session['ordemservico_id'] = self.kwargs.get('pk')
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def form_valid(self, form):
        proposta = form.save(commit=False)
        os = OrdemServico.objects.get(pk=self.request.session['ordemservico_id'])
        proposta.ordem_servico = os
        proposta.advogado = self.request.user.advogado
        del self.request.session['ordemservico_id']
        return super(PropostaCreate, self).form_valid(form)


class PropostaList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = '/login'
    permission_required = 'ordemservico.add_proposta'
    model = Proposta

    def get_queryset(self):
        if self.request.user.is_advogado:
            queryset = Proposta.objects.filter(advogado=self.request.user.advogado)
        elif self.request.user.is_empresa:
            queryset = Proposta.objects.filter(ordem_servico__empresa=self.request.user.empresa)
        else:
            queryset = Proposta.objects.all()
        return queryset


class PropostaAceita(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        proposta = Proposta.objects.get(pk=kwargs.get('pk'))
        proposta.status = 2
        proposta.save()

        os = OrdemServico.objects.get(pk=proposta.ordem_servico.pk)
        os.status = 2
        os.save()

        return redirect('/ordemservico/proposta/list')

class PropostaRecusada(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        proposta = Proposta.objects.get(pk=kwargs.get('pk'))
        proposta.status = 3
        proposta.save()

        os = OrdemServico.objects.get(pk=proposta.ordem_servico.pk)
        os.status = 3
        os.save()
        
        return redirect('/ordemservico/proposta/list')