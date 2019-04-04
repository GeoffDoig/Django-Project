from django import forms
from .models import Post


class BlogPostForm(forms.ModelForm):
    """ Form for users to create blog posts """
    class Meta:
        model = Post
        fields = ["title", "content", "tag"]
