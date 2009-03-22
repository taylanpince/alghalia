from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

from tagging.fields import TagField


class ArticleCategory(models.Model):
    """
    An article category
    """
    name = models.CharField(_("Name"), max_length=255)
    slug = models.SlugField(_("Slug"), max_length=255, unique=True)

    class Meta:
        verbose_name = _("Article Category")
        verbose_name_plural = _("Article Categories")

    def __unicode__(self):
        return self.name


class Article(models.Model):
    """
    An article, linked to a category
    """
    title = models.CharField(_("Title"), max_length=255)
    slug = models.SlugField(_("Slug"), max_length=255, unique=True)
    summary = models.TextField(_("Summary"), blank=True)
    body = models.TextField(_("Body"), blank=True)
    category = models.ForeignKey(ArticleCategory, verbose_name=_("Category"))
    tags = TagField(_("Tags"))

    featured = models.BooleanField(_("Featured"), default=False)
    published = models.BooleanField(_("Published"), default=True)
    publication_date = models.DateTimeField(_("Publication Date"), default=datetime.now)
    expiration_date = models.DateTimeField(_("Expiration Date"), blank=True, null=True)

    creation_date = models.DateTimeField(_("Creation Date"), editable=False, auto_now_add=True)
    modification_date = models.DateTimeField(_("Modification Date"), editable=False, auto_now=True)

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    def __unicode__(self):
        return self.title
