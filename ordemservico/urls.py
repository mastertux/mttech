from django.conf.urls import url

from ordemservico import views

urlpatterns = [
  url(r'^list$', views.OrdemServicoList.as_view(), name='ordemservico_list'),
  url(r'^new$', views.OrdemServicoCreate.as_view(), name='ordemservico_new'),
  url(r'^edit/(?P<pk>\d+)$', views.OrdemServicoUpdate.as_view(), name='ordemservico_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.OrdemServicoDelete.as_view(), name='ordemservico_delete'),
  url(r'^proposta/(?P<pk>\d+)$', views.PropostaCreate.as_view(), name='proposta_new'),
  url(r'^proposta/list$', views.PropostaList.as_view(), name='proposta_list'),
  url(r'^proposta/aceitar/(?P<pk>\d+)$', views.PropostaAceita.as_view(), name='proposta_aceita'),
  url(r'^proposta/recusar/(?P<pk>\d+)$', views.PropostaRecusada.as_view(), name='proposta_recusada'),
]