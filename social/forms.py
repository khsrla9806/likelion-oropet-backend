from django import forms
from .models import joinlist

class JoinForm(forms.ModelForm):
    class Meta:
        model = joinlist
        fields = ['username']