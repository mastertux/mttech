from django.conf.urls import url

from advogados import views

urlpatterns = [
  url(r'^list$', views.AdvogadosList.as_view(), name='advogados_list'),
  url(r'^new$', views.AdvogadosCreate.as_view(), name='advogados_new'),
  url(r'^edit/(?P<pk>\d+)$', views.AdvogadosUpdate.as_view(), name='advogados_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.AdvogadosDelete.as_view(), name='advogados_delete'),
]