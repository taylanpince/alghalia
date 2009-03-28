from django.conf.urls.defaults import *


urlpatterns = patterns('articles.views',
    url(r'^$', 'landing', name='articles_landing'),
    url(r'^search/$', 'search', name='articles_search'),
    url(r'^(?P<category_slug>[-\w]+)/$', 'archive', name='articles_archive_by_category'),
    url(r'^(?P<category_slug>[-\w]+)/(?P<year>\d{4})/$', 'archive', name='articles_archive_by_year'),
    url(r'^(?P<category_slug>[-\w]+)/(?P<year>\d{4})/(?P<month>\d{2})/$', 'archive', name='articles_archive_by_month'),
    url(r'^(?P<category_slug>[-\w]+)/(?P<year>\d{4})/(?P<month>\d{2})/(?P<slug>[-\w]+)/$', 'detail', name='articles_detail'),
)
