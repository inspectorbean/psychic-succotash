from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^data/$', views.data, name='data'),
    url(r'^bus_update/$', views.bus_update, name='bus_update')
    url(r'^$', views.bus, name='bus'),
]
