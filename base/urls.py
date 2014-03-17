__author__ = 'cuneyt'

from django.conf.urls import patterns, url
import views

urlpatterns = patterns(
    '',
    url(r'^$', views.home),
    url(r'^signup/$', views.signup),
    url(r'^login/$', views.login),
)
