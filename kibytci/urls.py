from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^ro$', views.ro_gismu),
    url(r'^comments/', include('django_comments.urls')),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', views.logout),
)

