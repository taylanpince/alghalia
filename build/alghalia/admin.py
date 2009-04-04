from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.admin import SiteAdmin
from django.contrib.sites.models import Site

from sharer.admin import SocialNetworkAdmin
from sharer.models import SocialNetwork

from articles.admin import ArticleAdmin, ArticleCategoryAdmin
from articles.models import Article, ArticleCategory
from comments.admin import CommentAdmin
from comments.models import Comment
from forms import FlatPageForm


class AlghaliaAdmin(admin.AdminSite):
    pass


alghalia_admin = AlghaliaAdmin()


class FlatPageAdmin(admin.ModelAdmin):
    form = FlatPageForm

    list_display = ("title", "url", )

    fieldsets = (
        (None, {
            "fields": (("title", "url", ), "content", "sites", )
        }),
    )


alghalia_admin.register(Article, ArticleAdmin)
alghalia_admin.register(ArticleCategory, ArticleCategoryAdmin)
alghalia_admin.register(Comment, CommentAdmin)
alghalia_admin.register(User, UserAdmin)
alghalia_admin.register(FlatPage, FlatPageAdmin)
alghalia_admin.register(Site, SiteAdmin)
