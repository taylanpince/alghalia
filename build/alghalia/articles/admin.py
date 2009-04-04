from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from articles.models import Article, ArticleCategory


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "featured", "theme", )
    list_filter = ["featured", "theme", ]

    save_on_top = True

    prepopulated_fields = {
        "slug": ("name", ),
    }

    fieldsets = (
        (None, {
            "fields": (("name", "slug", ), "theme", "featured", )
        }),
    )


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "featured", "published", "publication_date", "expiration_date", "creation_date", "modification_date", "view_count", )
    list_filter = ["featured", "published", ]

    search_fields = ("title", "subtitle", "summary", "body", "tags", )

    save_on_top = True

    prepopulated_fields = {
        "slug": ("title", ),
    }

    fieldsets = (
        (None, {
            "fields": (("title", "slug", ), "subtitle", "category", "summary", "body", "tags", )
        }),
        (_("Publication"), {
            "fields": ("featured", "published", "publication_date", "expiration_date", ),
            "classes": ("collapse", ),
        }),
    )


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
