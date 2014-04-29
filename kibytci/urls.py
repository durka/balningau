from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^ro$', views.ro_gismu),
    url(r'^comments/cikre/(?P<id>[0-9]+)/$', views.pinka_cikre),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^selstidi/(?P<id>[0-9]+)/$', views.selstidi),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', views.logout),
    url(r'^accounts/new/$', views.new_user),
)

