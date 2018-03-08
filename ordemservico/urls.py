from django.conf.urls import url

from ordemservico import views

urlpatterns = [
  url(r'^list$', views.OrdemServicoList.as_view(), name='ordemservico_list'),
  url(r'^new$', views.OrdemServicoCreate.as_view(), name='ordemservico_new'),
  url(r'^edit/(?P<pk>\d+)$', views.OrdemServicoUpdate.as_view(), name='ordemservico_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.OrdemServicoDelete.as_view(), name='ordemservico_delete'),
]