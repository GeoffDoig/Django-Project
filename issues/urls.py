from django.conf.urls import url
from .views import get_issues, show_issue

urlpatterns = [
    url(r'^all/', get_issues, name="issues"),
    url(r'^(?P<pk>\d+)$', show_issue, name="show_issue"),
    ]