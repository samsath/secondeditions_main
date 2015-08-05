# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.shortcuts import render_to_response
from django.template import RequestContext

def direct_to_template(request, template, **kwargs):
    return render_to_response(
        template,
        kwargs,
        context_instance=RequestContext(request))


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'website.frontpage.views.index', name='index'),


    #DEVELOPMENT
    #url(r'^$', direct_to_template, {'template': 'development/index.html'}, name='index'),


    url(r'^robots.txt$', 'django.shortcuts.render', {'template_name': 'robots.txt'},),
    url(r'^humans.txt$', 'django.shortcuts.render', {'template_name': 'humans.txt'},),

    # mediastore download counter
    url(r'^downloads/(?P<slug>[^/]+)/download/(?P<filename>.+)$', 'mediastore.mediatypes.download.views.download_counter', name='mediastore-download-link'),

    url(r'^admin/', include(admin.site.urls)),
   
)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^_403/$', 'django.shortcuts.render', {'template_name': '403.html'}),
        url(r'^_404/$', 'django.shortcuts.render', {'template_name': '404.html'}),
        url(r'^_500/$', 'django.shortcuts.render', {'template_name': '500.html'}),
        url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),


    )
