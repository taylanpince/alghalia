from django import forms
from django.utils.translation import ugettext_lazy as _

from tinymce.widgets import AdminTinyMCE

from articles.models import Article


class SearchForm(forms.Form):
    query = forms.CharField(label=_("Keywords"))


class ArticleForm(forms.ModelForm):
    summary = forms.CharField(label=_("Summary"), widget=AdminTinyMCE(attrs={
        "cols": 90,
        "rows": 15,
    }))

    body = forms.CharField(label=_("Body"), widget=AdminTinyMCE(attrs={
        "cols": 90,
        "rows": 40,
    }))

    class Meta:
        model = Article
