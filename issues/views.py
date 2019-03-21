from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Issue

# Create your views here.
def get_issues(request):
    """ Display all issues ordered by date reported """
    issues = Issue.objects.all().order_by("reported_date")
    return render(request, "issues.html", {"issues": issues})
    
def show_issue(request, pk):
    """ Display full details of a single issue """
    issue = get_object_or_404(Issue, pk=pk)
    return render(request, "issuedetail.html", {"issue": issue})
