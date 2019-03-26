from django.conf.urls import url
from .views import get_issues, show_issue, new_issue, display_screenshot

urlpatterns = [
    url(r'^all/', get_issues, name="issues"),
    url(r'^(?P<pk>\d+)$', show_issue, name="show_issue"),
    url(r'^new/', new_issue, name="new_issue"),
    url(r'^(?P<pk>\d+)/screenshot$', display_screenshot, name="screenshot"),
    ]