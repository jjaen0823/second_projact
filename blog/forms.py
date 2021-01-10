from django import forms
from .models import Blog


class BlogPost(forms.ModelForm):
    class Meta:
        models = Blog
        fields = ['title', 'content']
