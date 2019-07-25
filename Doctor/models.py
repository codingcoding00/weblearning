from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from django import forms




"""
#######################################



from collections import OrderedDict

from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import (
    UNUSABLE_PASSWORD_PREFIX, identify_hasher,
)
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.forms.utils import flatatt
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.html import format_html, format_html_join
from django.utils.http import urlsafe_base64_encode
from django.utils.safestring import mark_safe
from django.utils.text import capfirst
from django.utils.translation import ugettext, ugettext_lazy as _



class ReadOnlyPasswordHashWidget(forms.Widget):
    def render(self, name, value, attrs):
        encoded = value
        final_attrs = self.build_attrs(attrs)

        if not encoded or encoded.startswith(UNUSABLE_PASSWORD_PREFIX):
            summary = mark_safe("<strong>%s</strong>" % ugettext("No password set."))
        else:
            try:
                hasher = identify_hasher(encoded)
            except ValueError:
                summary = mark_safe("<strong>%s</strong>" % ugettext(
                    "Invalid password format or unknown hashing algorithm."))
            else:
                summary = format_html_join('',
                                           "<strong>{}</strong>: {} ",
                                           ((ugettext(key), value)
                                            for key, value in hasher.safe_summary(encoded).items())
                                           )

        return format_html("<div{}>{}</div>", flatatt(final_attrs), summary)


class ReadOnlyPasswordHashField(forms.Field):
    widget = ReadOnlyPasswordHashWidget

"""
######################################
# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    certficate = models.FileField()
    active = models.BooleanField(default = False)
    validity = models.BooleanField(default = False)
    patientName = models.CharField(default='patient',max_length=100)
    time_book1_model = models.CharField(default='time',max_length=10)
    #book_user_id = {}
    #time_book = {}
    rating = models.FloatField(default=0)
    profile = models.CharField(max_length=100, default='')
    
    location = models.CharField(max_length = 200, default='loc')
    available_dates = models.CharField(max_length=200, default='date')
    works_from = models.IntegerField(default=0)
    works_upto = models.IntegerField(default=0)
    curr_status = models.IntegerField(default=0)
    max_status = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('divaDoc:home')

    def __str__(self):
        return self.name