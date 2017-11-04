from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^d/(?P<d_id>\d+)/$', views.dinner_detail, name='dinner_detail'),
    url(r'^add-rest/$', views.add_rest, name='add_rest'),
    url(r'^add-dinner/$', views.add_dinner, name='add_dinner'),
    url(r'^$', views.eatout_home, name='eatout_home'),
]
