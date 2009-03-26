from django import template
from django.contrib.contenttypes.models import ContentType

from comments.forms import CommentForm
from comments.models import Comment


register = template.Library()


@register.inclusion_tag("comments/includes/form.html", takes_context=True)
def comment_form(context, object):
    """
    Renders a comment form for the given object
    """
    form = CommentForm(auto_id="%s", prefix="CommentForm", initial={
        "content_type_id": ContentType.objects.get_for_model(object).pk,
        "object_id": object.pk,
        "author": context.get("COMMENT_AUTHOR", ""),
        "email": context.get("COMMENT_EMAIL", ""),
        "remember": context.get("COMMENT_EMAIL", None) or context.get("COMMENT_AUTHOR", None),
    })

    return {
        "form": form,
        "object": object,
        "MEDIA_URL": context.get("MEDIA_URL", None),
    }


@register.inclusion_tag("comments/includes/list.html", takes_context=True)
def comments(context, object):
    """
    Renders a list of comments for a given object
    """
    comments = Comment.objects.get_for_model(object)

    return {
        "object": object,
        "comments": comments,
    }
