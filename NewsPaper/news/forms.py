from django import forms
from django.core.exceptions import ValidationError

from .models import Post, Category


class PostForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = ['author', 'products', 'title_news', 'text_news', 'post_reiting']

