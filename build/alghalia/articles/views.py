from datetime import datetime

from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import simple, list_detail

from articles.forms import SearchForm
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


def search(request):
    """
    Renders search results
    """
    form = SearchForm(request.GET, auto_id="SearchForm-%s")

    if form.is_valid():
        query = form.cleaned_data.get("query")
        articles = Article.objects.filter(
            Q(title__icontains=query) | 
            Q(subtitle__icontains=query) | 
            Q(summary__icontains=query) | 
            Q(tags__icontains=query) | 
            Q(body__icontains=query)
        )
    else:
        query = None
        articles = None

    return list_detail.object_list(
        request,
        queryset=articles,
        paginate_by=10,
        template_name="articles/search.html",
        template_object_name="articles",
        extra_context={
            "query": query,
        }
    )


def archive(request, category_slug, year=None, month=None):
    """
    Archive page that can filter by category, year and month
    """
    category = get_object_or_404(ArticleCategory, slug__iexact=category_slug)
    articles = Article.objects.filter(category=category)
    active_date = None

    if year:
        articles = articles.filter(publication_date__year=int(year))

        active_date = datetime(int(year), 1, 1, 0, 0)

    if month:
        articles = articles.filter(publication_date__month=int(month))

        active_date = datetime(int(year), int(month), 1, 0, 0)

    return list_detail.object_list(
        request,
        queryset=articles,
        paginate_by=10,
        template_name="articles/archive.html",
        template_object_name="articles",
        extra_context={
            "category": category,
            "year": year,
            "month": month,
            "active_date": active_date,
        }
    )


def detail(request, category_slug, year, month, slug):
    """
    Detail page for an article
    """
    category = get_object_or_404(ArticleCategory, slug__iexact=category_slug)
    article = get_object_or_404(Article.objects, 
        category=category, 
        publication_date__year=int(year), 
        publication_date__month=int(month), 
        slug__iexact=slug
    )

    article.view_count += 1
    article.save()

    return simple.direct_to_template(request, "articles/detail.html", {
        "category": category,
        "article": article,
    })
