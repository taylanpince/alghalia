from django import forms
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _

from captcha.fields import CaptchaField

from comments.models import Comment


class CommentForm(forms.ModelForm):
    """
    A comment form
    """
    remember = forms.BooleanField(label=_("Remember me"), required=False)
    content_type_id = forms.IntegerField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    captcha = CaptchaField(label=_("Verification"))

    class Meta:
        model = Comment
        fields = ("title", "body", "author", "email", "object_id", )

    def save(self, commit=True):
        """
        Creates a Comment object with generic content type data
        """
        comment = super(CommentForm, self).save(commit=False)
        comment.content_type = ContentType.objects.get(pk=self.cleaned_data.get("content_type_id"))
        comment.obj = comment.content_type.get_object_for_this_type(pk=self.cleaned_data.get("object_id"))

        if commit:
            comment.save()

        return comment
