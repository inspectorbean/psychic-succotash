from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^d/(?P<d_id>\d+)/$', views.dinner_detail, name='dinner_detail'),
    url(r'^d/e/(?P<d_id>\d+)/$', views.edit_dinner, name='edit_dinner'),
    url(r'^r/(?P<r_id>\d+)/$', views.rest_detail, name='rest_detail'),
    url(r'^r/e/(?P<r_id>\d+)/$', views.edit_rest, name='edit_rest'),
    url(r'^add-rest/$', views.add_rest, name='add_rest'),
    url(r'^add-dinner/$', views.add_dinner, name='add_dinner'),
    url(r'^$', views.eatout_home, name='eatout_home'),
]
