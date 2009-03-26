from django.http import HttpResponseRedirect
from django.views.generic import simple

from comments.forms import CommentForm
from comments.models import Comment


def show_comment(request, id):
    """
    Renders a single comment
    """
    pass


def post_comment(request):
    """
    Handles comment submissions
    """
    form = CommentForm(request.POST, auto_id="%s", prefix="CommentForm")

    if form.is_valid():
        comment = form.save(commit=False)
        comment.ip_address = request.META.get("REMOTE_ADDR", None)

        comment.save()

        if not request.is_ajax():
            return HttpResponseRedirect(comment.get_absolute_url())

    return simple.direct_to_template(request, "comments/form.html", {
        "form": form,
    })
