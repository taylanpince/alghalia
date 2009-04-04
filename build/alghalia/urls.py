from django.conf.urls.defaults import *

from admin import alghalia_admin
from articles.feeds import RssLatestArticles, RssLatestArticlesByCategory


urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/filebrowser/', include('filebrowser.urls')),
    (r'^admin/tinymce/', include('tinymce.urls')),
    (r'^admin/(.*)', alghalia_admin.root),

    (r'^captcha/', include('captcha.urls')),
    (r'^share/', include('sharer.urls')),

    (r'^articles/', include('articles.urls')),
    (r'^comments/', include('comments.urls')),
    
    url(r'^$', 'django.views.generic.simple.direct_to_template', {
        'template': 'home.html',
    }, name='home'),

    url(r"^feeds/(?P<url>.*)/$", "django.contrib.syndication.views.feed", {
        "feed_dict": {
            "articles": RssLatestArticles,
            "articles-by-category": RssLatestArticlesByCategory,
        },
    }, name="feeds"),
)
