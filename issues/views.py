from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Issue
from .forms import CommentsForm, NewIssueForm

# Create your views here.
def get_issues(request):
    """ Display all issues ordered by date reported """
    issues = Issue.objects.all().order_by("reported_date")
    return render(request, "issues.html", {"issues": issues})
    
def show_issue(request, pk):
    """ Display full details of a single issue """
    issue = get_object_or_404(Issue, pk=pk)
    user = User.objects.get(email=request.user.email)
    if request.method == "POST":
        form = CommentsForm(request.POST, initial={"username": user, "comment_date": timezone.now})
        if form.is_valid():
            form = issue.comments
            issue.save(update_fields=["comments"])
            return redirect(reverse(get_issues))
    else:
        form = CommentsForm(initial={"username": user, "comment_date": timezone.now})
    return render(request, "issuedetail.html", {"issue": issue, "form": form})

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
    
