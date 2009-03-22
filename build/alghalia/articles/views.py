from django.shortcuts import get_object_or_404
from django.views.generic import simple, list_detail

from articles.models import Article, ArticleCategory


def landing(request):
    """
    Landing page for articles, lists latest articles in all categories
    """
    articles = Article.objects.all()
    categories = ArticleCategory.objects.all()

    return simple.direct_to_template(request, "articles/landing.html", {
        "articles": articles,
        "categories": categories,
    })


def archive(request, category_slug, year=None, month=None):
    """
    Archive page that can filter by category, year and month
    """
    category = get_object_or_404(ArticleCategory, slug__iexact=category_slug)
    articles = Article.objects.filter(category=category)

    if year:
        articles = articles.filter(publication_date__year=int(year))

    if month:
        articles = articles.filter(publication_date__month=int(month))

    return list_detail.object_list(
        request,
        queryset=articles,
        paginate_by=10,
        template_name="articles/archive.html",
        template_object_name="articles",
        extra_context={
            "category": category,
        }
    )


def detail(request, category_slug, year, month, slug):
    """
    Detail page for an article
    """
    category = get_object_or_404(ArticleCategory, slug__iexact=category_slug)
    article = get_object_or_404(Article.objects, category=category, year=int(year), month=int(month), slug__iexact=slug)

    article.view_count += 1
    article.save()

    return simple.direct_to_template(request, "articles/detail.html", {
        "category": category,
        "article": article,
    })
