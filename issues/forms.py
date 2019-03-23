from django import forms
from .models import Issue, Comments

class CommentsForm(forms.ModelForm):
    """ Form for users to add their comments to specific issues """
    class Meta:
        model = Comments
        fields = ("comment", "username")
        widgets = {"username": forms.TextInput(attrs={'readonly': True})}
    
class NewIssueForm(forms.ModelForm):
    """ Form for user to create new issues on the website """
    class Meta:
        model = Issue
        fields = ("title", "description", "screenshot", "username")
        widgets = {"username": forms.TextInput(attrs={'readonly': True})}
    