from django.contrib import admin
from django.utils.translation import ugettext_lazy as _, ugettext

from batchadmin.admin import BatchModelAdmin, CHECKBOX_NAME

from comments.models import Comment


class CommentAdmin(BatchModelAdmin):
    list_display = ("pk", "author", "email", "title", "body", "creation_date", "modification_date", "published", )
    list_filter = ["published", ]
    
    search_fields = ("author", "email", "title", "body", )
    
    save_on_top = True
    
    fieldsets = (
        (_("Content"), {
            "fields": ("title", "body", "published", ),
        }),
        (_("Author"), {
            "fields": ("author", "email", "ip_address", ),
        }),
        (_("Relations"), {
            "fields": ("content_type", "object_id", ),
            "classes": ["collapse", ],
        }),
    )

    batch_actions = ["delete_selected", "publish_selected", "unpublish_selected"]

    def update_publication_status(self, request, changelist, status):
        """
        Updates the publication status of the selected items
        """
        selected = request.POST.getlist(CHECKBOX_NAME)
        objects = changelist.get_query_set().filter(pk__in=selected)

        for obj in objects:
            obj.published = status
            obj.save()

    def publish_selected(self, request, changelist):
        """
        Publish selected items
        """
        self.update_publication_status(request, changelist, True)
        self.message_user(request, ugettext("Selected comments have been published."))

    def unpublish_selected(self, request, changelist):
        """
        Unpublish selected items
        """
        self.update_publication_status(request, changelist, False)
        self.message_user(request, ugettext("Selected comments have been unpublished."))

    publish_selected.short_description = _("Publish selected %(verbose_name_plural)s")
    unpublish_selected.short_description = _("Unpublish selected %(verbose_name_plural)s")


admin.site.register(Comment, CommentAdmin)
