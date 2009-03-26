from django import template
from django.contrib.contenttypes.models import ContentType

from comments.forms import CommentForm
from comments.models import Comment


register = template.Library()


@register.inclusion_tag("comments/form.html", takes_context=True)
def comment_form(context, object):
    """
    Renders a comment form for the given object
    """
    form = CommentForm(auto_id="%s", prefix="CommentForm", initial={
        "content_type_id": ContentType.objects.get_for_model(object).pk,
        "object_id": object.pk,
    })

    return {
        "form": form,
        "object": object,
        "MEDIA_URL": context.get("MEDIA_URL", None),
    }
