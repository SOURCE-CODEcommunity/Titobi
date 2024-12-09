from django import forms
from . import models

class CreatePosts(forms.ModelForm):
    class Meta:
        model = models.post
        fields = ['title', 'body', 'slug', 'banner']