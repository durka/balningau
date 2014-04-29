from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from kibytci import urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'balningau.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^kibytci/', include('kibytci.urls')),
    url(r'^password/', include('password_reset.urls')),
)
