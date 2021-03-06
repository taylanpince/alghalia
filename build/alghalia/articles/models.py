from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

from tagging.fields import TagField

from articles.managers import ArticleManager


THEME_CHOICES = (
    ("green", _("Green")),
    ("turquoise", _("Turquoise")),
    ("purple", _("Purple")),
)


class ArticleCategory(models.Model):
    """
    An article category
    """
    name = models.CharField(_("Name"), max_length=255)
    slug = models.SlugField(_("Slug"), max_length=255, unique=True)
    theme = models.CharField(_("Colour Theme"), max_length=10, choices=THEME_CHOICES)
    featured = models.BooleanField(_("Featured"), default=False)
    order = models.PositiveSmallIntegerField(_("Order"), default=0)
    parent = models.ForeignKey("self", verbose_name=_("Parent Category"), limit_choices_to={
        "parent__isnull": True,
    }, blank=True, null=True, related_name="sub_categories")

    class Meta:
        ordering = ["order"]
        verbose_name = _("Article Category")
        verbose_name_plural = _("Article Categories")

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ("articles_archive_by_category", (), {
            "category_slug": self.slug,
        })


class Article(models.Model):
    """
    An article, linked to a category
    """
    title = models.CharField(_("Title"), max_length=255)
    slug = models.SlugField(_("Slug"), max_length=255)
    subtitle = models.CharField(_("Sub Title"), max_length=255, blank=True)
    summary = models.TextField(_("Summary"), blank=True)
    body = models.TextField(_("Body"), blank=True)
    category = models.ForeignKey(ArticleCategory, verbose_name=_("Category"))
    author = models.ForeignKey("auth.User", related_name=_("Author"), blank=True, null=True)
    tags = TagField(_("Tags"))

    featured = models.BooleanField(_("Featured"), default=False)
    published = models.BooleanField(_("Published"), default=True)
    publication_date = models.DateTimeField(_("Publication Date"), default=datetime.now)
    expiration_date = models.DateTimeField(_("Expiration Date"), blank=True, null=True)

    creation_date = models.DateTimeField(_("Creation Date"), editable=False, auto_now_add=True)
    modification_date = models.DateTimeField(_("Modification Date"), editable=False, auto_now=True)
    view_count = models.PositiveIntegerField(_("View Count"), editable=False, default=0)

    admin_objects = models.Manager()
    objects = ArticleManager()

    class Meta:
        ordering = ["-publication_date", "-id"]
        unique_together = (("slug", "publication_date", "category", ), )
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ("articles_detail", (), {
            "category_slug": self.category.slug,
            "year": self.publication_date.year,
            "month": self.publication_date.strftime("%m"),
            "slug": self.slug,
        })

    @property
    def author_name(self):
        if self.author.first_name and self.author.last_name:
            return "%s %s" % (self.author.first_name, self.author.last_name)
        elif self.author.first_name or self.author.last_name:
            return self.author.first_name or self.author.last_name
        else:
            return self.author.username
