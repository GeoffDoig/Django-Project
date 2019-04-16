from django import forms
from .models import Issue, Comment


class CommentsForm(forms.ModelForm):
    """
    Form for users to add their comments to specific issues
    """
    class Meta:
        model = Comment
        fields = ["comment"]


class NewIssueForm(forms.ModelForm):
    """
    Form for user to create new issues on the website
    """
    class Meta:
        model = Issue
        fields = ["title", "category", "description", "screenshot"]
