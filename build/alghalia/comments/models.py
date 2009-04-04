from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _

from comments.managers import CommentManager


class Comment(models.Model):
    """
    A comment linked to a generic object
    """
    title = models.CharField(_("Title"), max_length=255, blank=True)
    body = models.TextField(_("Comment"))
    published = models.BooleanField(_("Published"), default=False)

    author = models.CharField(_("Name"), blank=True, max_length=255)
    email = models.EmailField(_("Email"), blank=True)
    ip_address = models.IPAddressField(_("IP Address"), blank=True, null=True)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    obj = generic.GenericForeignKey()

    creation_date = models.DateTimeField(_("Creation Date"), editable=False, auto_now_add=True)
    modification_date = models.DateTimeField(_("Modification Date"), editable=False, auto_now=True)

    admin_objects = models.Manager()
    objects = CommentManager()

    class Meta:
        ordering = ["creation_date", "id"]
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
    
    def __unicode__(self):
        return u"Comment on %(date)s for %(obj)s" % {
            "date": self.creation_date,
            "obj": self.obj,
        }

    def get_absolute_url(self):
        return self.obj.get_absolute_url() + "#comment-%d" % self.pk

    @property
    def author_name(self):
        return self.author or _("Anonymous")
