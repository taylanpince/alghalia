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
    pass
