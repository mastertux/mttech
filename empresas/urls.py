from django.conf.urls import url

from empresas import views

urlpatterns = [
  url(r'^list$', views.EmpresasList.as_view(), name='empresas_list'),
  url(r'^new$', views.EmpresasCreate.as_view(), name='empresas_new'),
  url(r'^edit/(?P<pk>\d+)$', views.EmpresasUpdate.as_view(), name='empresas_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.EmpresasDelete.as_view(), name='empresas_delete'),
]