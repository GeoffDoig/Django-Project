from django import forms
from .models import Issue

class CommentsForm(forms.Form):
    """ Form for users to add their comments to specific issues """
    comment = forms.CharField(widget=forms.Textarea, label="Add a Comment")
    username = forms.CharField(max_length=30, disabled=True)
    comment_date = forms.DateTimeField(disabled=True)
    
class NewIssueForm(forms.ModelForm):
    """ Form for user to create new issues on the website """
    class Meta:
        model = Issue
        fields = ("title", "description", "screenshot", "username")
        widgets = {"username": forms.TextInput(attrs={'readonly': True})}
    