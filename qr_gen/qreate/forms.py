from dataclasses import field, fields
from socket import fromshare
from django import forms
from django.forms import ModelForm
from .models import Webqr

# creating our form
class UrlForm(ModelForm):
    class Meta:
        model = Webqr
        fields = ('name',)
