from django import template

from articles.models import Article


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
