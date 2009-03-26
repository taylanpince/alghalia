from django.conf.urls.defaults import *


urlpatterns = patterns('comments.views',
    url(r'^post/$', 'post_comment', name='comments_post'),
    url(r'^show/(?P<id>\d+)/$', 'show_comment', name='comments_show'),
)
