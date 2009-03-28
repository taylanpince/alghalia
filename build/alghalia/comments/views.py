from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils import simplejson
from django.views.generic import simple

from comments.encoders import LazyEncoder
from comments.forms import CommentForm
from comments.models import Comment


def show_comment(request, id):
    """
    Renders a single comment
    """
    comment = get_object_or_404(Comment.objects, pk=id)

    if request.is_ajax():
        template = "comments/includes/detail.html"
    else:
        template = "comments/detail.html"

    return simple.direct_to_template(request, template, {
        "comment": comment,
    })


def post_comment(request):
    """
    Handles comment submissions
    """
    form = CommentForm(request.POST, auto_id="%s", prefix="CommentForm")

    if form.is_valid():
        comment = form.save(commit=False)
        comment.ip_address = request.META.get("REMOTE_ADDR", None)

        comment.save()

        if request.is_ajax():
            response = simple.direct_to_template(request, "comments/form.json", {
                "comment": comment,
                "total": Comment.objects.get_for_model(comment.obj).count(),
            }, mimetype="application/json")
        else:
            response = HttpResponseRedirect(comment.get_absolute_url())

        if form.cleaned_data.get("remember", False):
            response.set_cookie("comment_author", value=comment.author)
            response.set_cookie("comment_email", value=comment.email)
        else:
            response.delete_cookie("comment_author")
            response.delete_cookie("comment_email")

        return response
    else:
        if request.is_ajax():
            if form.errors:
                errors = simplejson.dumps(form.errors, cls=LazyEncoder, ensure_ascii=False)
            else:
                errors = None

            template = "comments/form.json"
            mimetype = "application/json"
        else:
            errors = None
            template = "comments/form.html"
            mimetype = None

        return simple.direct_to_template(request, template, {
            "form": form,
            "errors": errors,
            "total": 0,
        }, mimetype=mimetype)
