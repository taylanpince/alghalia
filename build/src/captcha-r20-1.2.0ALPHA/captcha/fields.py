import datetime

from captcha.conf import settings
from django.core.urlresolvers import reverse
from django.forms.fields import CharField, MultiValueField
from django.forms import ValidationError
from django.forms.widgets import TextInput, MultiWidget, HiddenInput
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from captcha.helpers import *
from captcha.models import CaptchaStore


class CaptchaTextInput(MultiWidget):
    def __init__(self,attrs=None):
        widgets = (
            HiddenInput(attrs),
            TextInput(attrs),
        )

        super(CaptchaTextInput,self).__init__(widgets,attrs)

    def decompress(self,value):
        if value:
            return value.split(',')

        return [None, None]

    def render(self, name, value, attrs=None):
        challenge,response= settings.get_challenge()()

        store, created = CaptchaStore.objects.get_or_create(challenge=challenge,response=response)
        key = store.hashkey
        value = [key, u'']

        return render_to_string("captcha/captcha.html", {
            "key": key,
            "flite": settings.CAPTCHA_FLITE_PATH,
            "field": super(CaptchaTextInput, self).render(name, value, attrs=attrs),
        })


class CaptchaField(MultiValueField):
    default_error_messages = {
        'invalid': _("The code you entered is not valid, please enter the characters exactly as you see them in the image."),
    }
    widget = CaptchaTextInput

    def __init__(self, *args,**kwargs):
        fields = (
            CharField(show_hidden_initial=True), 
            CharField(),
        )

        super(CaptchaField,self).__init__(fields=fields, *args, **kwargs)

    def compress(self,data_list):
        if data_list:
            return ','.join(data_list)

        return None
        
    def clean(self, value):
        super(CaptchaField, self).clean(value)

        response, value[1] = value[1].strip().lower(), ''

        CaptchaStore.remove_expired()

        try:
            store = CaptchaStore.objects.get(response=response,hashkey=value[0], expiration__gt=datetime.datetime.now())
            store.delete()
        except Exception:
            raise ValidationError(self.error_messages['invalid'])

        return value
