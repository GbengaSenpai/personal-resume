from django import forms
from django.forms.fields import CharField

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=50)
    message = forms.CharField(widget = forms.Textarea, max_length=2000)
    