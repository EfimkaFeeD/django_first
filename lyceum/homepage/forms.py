__all__ = ["EchoForm"]

from django import forms


class EchoForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
