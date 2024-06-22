# forms.py
from django import forms

class PhishingEmailTemplateForm(forms.Form):
    subject = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    attachment = forms.FileField(required=False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))
