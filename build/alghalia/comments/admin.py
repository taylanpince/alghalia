from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from comments.models import Comment


class CommentAdmin(admin.ModelAdmin):
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


admin.site.register(Comment, CommentAdmin)
