from django.conf.urls.defaults import *
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),

    (r'^articles/', include('articles.urls')),
    
    url(r'^$', 'django.views.generic.simple.direct_to_template', {
        'template': 'home.html',
    }, name='home')
)
