from django.shortcuts import render

# Create your views here.
def get_issues(request):
    """ Display all issues """
    return render(request, "issues.html")
