from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from articles.forms import ArticleForm
from articles.models import Article, ArticleCategory


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "featured", "theme", "order", )
    list_filter = ["featured", "theme", ]

    save_on_top = True

    prepopulated_fields = {
        "slug": ("name", ),
    }

    fieldsets = (
        (None, {
            "fields": (("name", "slug", ), "parent", "theme", "featured", "order", )
        }),
    )


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm

    list_display = ("title", "author", "featured", "published", "publication_date", "expiration_date", "creation_date", "modification_date", "view_count", )
    list_filter = ["featured", "published", ]

    date_hierarchy = "publication_date"
    ordering = ["-publication_date"]

    search_fields = ("title", "subtitle", "summary", "body", "tags", )

    save_on_top = True

    prepopulated_fields = {
        "slug": ("title", ),
    }

    fieldsets = (
        (None, {
            "fields": (("title", "slug", ), "subtitle", "category", "summary", "body", "author", "tags", )
        }),
        (_("Publication"), {
            "fields": ("featured", "published", "publication_date", "expiration_date", ),
            "classes": ("collapse", ),
        }),
    )

    def save_model(self, request, obj, form, change):
        if not obj.author or (not change and not obj.author):
            obj.author = request.user

        obj.save()
