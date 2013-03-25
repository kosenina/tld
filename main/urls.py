__author__ = 'Luka'

from django.conf.urls import patterns, url
from main import views

urlpatterns = patterns('',
    url(r'^login/$', views.login, name='login'),
    url(r'^home/$', views.home, name='home'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^article$', views.article, name='article')
)