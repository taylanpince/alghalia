from django.conf.urls.defaults import *


urlpatterns = patterns('comments.views',
    url(r'^post/$', 'post_comment', name='comments_post'),
    url(r'^captcha/$', 'generate_comment_captcha', name='comments_captcha'),
    url(r'^show/(?P<id>\d+)/$', 'show_comment', name='comments_show'),
)
