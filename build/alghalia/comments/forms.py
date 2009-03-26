from django import forms
from django.utils.translation import ugettext_lazy as _

from comments.models import Comment


class CommentForm(forms.ModelForm):
    """
    A comment form
    """
    remember = forms.BooleanField(label=_("Remember me"), required=False)
    content_type_id = forms.IntegerField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)

    class Meta:
        model = Comment
        fields = ("body", "author", "email", "object_id", )
