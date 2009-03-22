from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from articles.models import Article, ArticleCategory


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", )
    prepopulated_fields = {
        "slug": ("name", ),
    }


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "featured", "published", "publication_date", "expiration_date", "creation_date", "modification_date", )
    list_filter = ("featured", "published", )
    prepopulated_fields = {
        "slug": ("title", ),
    }
    
    fieldsets = (
        (None, {
            "fields": (("title", "slug", ), "category", "summary", "body", "tags", )
        }),
        (_("Publication"), {
            "fields": ("featured", "published", "publication_date", "expiration_date", ),
            "classes": ("collapse", ),
        }),
    )


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)