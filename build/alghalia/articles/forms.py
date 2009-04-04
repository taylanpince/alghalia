from django import forms
from django.utils.translation import ugettext_lazy as _

from tinymce.widgets import TinyMCE

from articles.models import Article


class SearchForm(forms.Form):
    query = forms.CharField(label=_("Keywords"))


class ArticleForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCE(attrs={
        "cols": 80,
        "rows": 30,
    }))

    class Meta:
        model = Article
