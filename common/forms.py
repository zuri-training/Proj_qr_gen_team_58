from django import forms
from . import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contacts
        fields = "__all__"
