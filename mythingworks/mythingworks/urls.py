from django.conf.urls import patterns, include, url
from store import urls as app_urls
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mythingworks.views.home', name='home'),
    # url(r'^mythingworks/', include('mythingworks.foo.urls')),
    url(r'^',include(app_urls)),
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
