from django import forms
from django.utils.translation import ugettext_lazy as _


class SearchForm(forms.Form):
    query = forms.CharField(label=_("Keywords"))
