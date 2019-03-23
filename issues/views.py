from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Issue, Comments
from .forms import CommentsForm, NewIssueForm

# Create your views here.
entries = []

def get_issues(request):
    """ Display all issues ordered by date reported """
    issues = Issue.objects.all().order_by("reported_date")
    comments = entries.count(entries)
    return render(request, "issues.html", {"issues": issues, "comments": comments})
    
def show_issue(request, pk):
    """ Display full details of a single issue """
    issue = get_object_or_404(Issue, pk=pk)
    if request.user.is_authenticated:
        user = User.objects.get(email=request.user.email)
        if request.method == "POST":
            form = CommentsForm(request.POST, initial={"username": user})
            if form.is_valid():
                entries.append(form)
                form.save()
                form = CommentsForm(initial={"username": user})
                return render(request, "issuedetail.html", {"issue": issue, "form": form, "entries": entries})
        else:
            form = CommentsForm(initial={"username": user})
            return render(request, "issuedetail.html", {"issue": issue, "form": form})
    else:
        return render(request, "issuedetail.html", {"issue": issue})

@login_required    
def new_issue(request):
    """ Provide a form for users to complete to create new issues """
    user = User.objects.get(email=request.user.email)
    if request.method == "POST":
        form = NewIssueForm(request.POST, request.FILES, initial={"username": user})
        if form.is_valid():
            form.save()
            messages.success(request, "Your issue has been created successfully")
            return redirect(get_issues)
        else:
            messages.error(request, "Unable to create issue at this time")
    else:
        form = NewIssueForm(initial={"username": user})
    return render(request, "newissue.html", {"form": form})
    
