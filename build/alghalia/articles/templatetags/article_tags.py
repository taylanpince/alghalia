import re

from django import template

from articles.models import Article, ArticleCategory


register = template.Library()


@register.inclusion_tag("articles/includes/months.html")
def article_months(category):
    """
    Render a list of months for all articles or for a given category
    """
    months = Article.objects.filter(category=category).dates("publication_date", "month")

    return {
        "category": category,
        "months": months,
    }


@register.inclusion_tag("articles/includes/latest.html")
def latest_article(category=None):
    """
    Gets the latest article, optionally filtered by category
    """
    articles = Article.objects.all()

    if category:
        articles = Article.objects.filter(category=category)

    try:
        article = articles.latest("publication_date")
    except Article.DoesNotExist:
        article = None

    return {
        "category": category,
        "article": article,
    }


@register.inclusion_tag("articles/includes/popular.html")
def popular_articles(category=None):
    """
    Gets the most popular articles, optionally filtered by category
    """
    articles = Article.objects.all()

    if category:
        articles = Article.objects.filter(category=category)

    articles = articles.order_by("-view_count")

    return {
        "category": category,
        "articles": articles,
    }


class FeaturedCategoriesNode(template.Node):
    def __init__(self, var_name):
        self.var_name = var_name

    def render(self, context):
        categories = ArticleCategory.objects.filter(featured=True)

        context[self.var_name] = categories

        return ""


@register.tag
def get_featured_categories(parser, token):
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires arguments" % token.contents.split()[0]

    m = re.search(r"as (\w+)", arg)

    if not m:
        raise template.TemplateSyntaxError, "%r tag had invalid arguments" % tag_name

    var_name, = m.groups()

    return FeaturedCategoriesNode(var_name)
