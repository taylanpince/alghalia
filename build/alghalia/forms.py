from django import forms
from django.utils.translation import ugettext_lazy as _

from tinymce.widgets import AdminTinyMCE

from django.contrib.flatpages.models import FlatPage


class FlatPageForm(forms.ModelForm):
    content = forms.CharField(label=_("Content"), widget=AdminTinyMCE(attrs={
        "cols": 90,
        "rows": 40,
    }))

    class Meta:
        model = FlatPage
