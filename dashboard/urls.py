from django.conf.urls import url

from dashboard import views

urlpatterns = [
  url(r'', views.index, name='dashboard'),
  url(r'^new$', views.DashboardCreate.as_view(), name='dashboard_new'),
  url(r'^edit/(?P<pk>\d+)$', views.DashboardUpdate.as_view(), name='dashboard_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.DashboardDelete.as_view(), name='dashboard_delete'),
]
