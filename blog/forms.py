from django import forms
from .models import Post

class BlogPostForm(forms.ModelForm):
    """ Form for users to create blog posts """
    class Meta:
        model = Post
        fields = ["title", "content", "author", "avatar", "tag"]
        widgets = {"author": forms.TextInput(attrs={'readonly': True})}
        