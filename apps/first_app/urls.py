from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<test>\d+)$', views.show),
    url(r'^(?P<test>\d+)/edit$', views.edit),
    url(r'^(?P<test>\d+)/delete$', views.destroy)
]                         