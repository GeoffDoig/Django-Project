from django.conf.urls import url
from .views import get_issues

urlpatterns = [
    url(r'^all/', get_issues, name="issues")
    ]