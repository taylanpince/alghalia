from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from django.contrib.syndication.feeds import Feed, FeedDoesNotExist
from django.utils.feedgenerator import Atom1Feed

from articles.models import Article, ArticleCategory


class RssLatestArticles(Feed):
    title_template = "feeds/article_title.html"
    description_template = "feeds/article_description.html"
    
    feed_type = Atom1Feed
    
    title = "Alghalia - Latest Articles"
    subtitle = "Latest articles from alghalia.net"
    author_name = "Alghalia"
    copyright = "Copyright (c) 2009, Alghalia"
    
    def link(self):
        return "http://%s%s" % (Site.objects.get_current().domain, reverse("articles_landing"))
    
    def items(self):
        return Article.objects.all()[:15]
    
    def item_pubdate(self, item):
        return item.publication_date
    
    def item_categories(self, item):
        return [item.category]


class RssLatestArticlesByCategory(RssLatestArticles):
    def title(self, obj):
        return "Alghalia - Articles Listed Under %s" % obj.name
    
    def description(self, obj):
        return "Latest articles listed under %(category)s from alghalia.net" % {
            "category": obj.name,
        }
    
    def link(self, obj):
        if not obj:
            raise FeedDoesNotExist
        
        return reverse("articles_archive_by_category", kwargs={
            "category_slug": obj.slug,
        })
    
    def get_object(self, bits):
        if len(bits) != 1:
            raise ObjectDoesNotExist
        
        return ArticleCategory.objects.get(slug__exact=bits[0])
    
    def items(self, obj):
        return Article.objects.filter(category=obj)[:15]
