from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^ro$', views.ro_gismu),
)

