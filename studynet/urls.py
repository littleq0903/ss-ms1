from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # note: In my concepts about individual client/server application,
    # the bootstrap server should be a separated process, 
    # and should handle both client/server boostraping.
    #   
    # This is just for compromising with usual server-side frameworks.
    # And will only bootstrap the client application.
    url(r'^bootstrap/$', 'bootstrap.views.ship'),
#    url(r'^$', 'bootstrap.views.ship'),

    # Module View
    (r'^courses/', include('courses.urls')),
)

urlpatterns += patterns('',
    (r'^accounts/', include('userena.urls')),
)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
    (r'^yknow_api/$', 'globals.views.yknow_api'),

    (r'^prototype/', TemplateView.as_view(template_name="prototype.html")),
    (r'^channel\.html', TemplateView.as_view(template_name="fb/channel.html")),
    (r'^favicon\.ico', RedirectView.as_view, {'url': '/static/img/favicon.ico'}),
    (r'^$', TemplateView.as_view(template_name="home.html")),
)

# for django_facebook

