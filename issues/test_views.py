from django.test import TestCase
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Issue, Comment


class TestIssuesViews(TestCase):
    def setUp(self):
        user = User(username="Name")
        user.save()
        self.client.force_login(user)

    def test_show_issues_page(self):
        page = self.client.get("/issues/all/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "issues.html")

    def test_show_screenshot_page(self):
        issue = Issue(title="Test Issue", screenshot="Test.jpg")
        issue.save()
        page = self.client.get("/issues/{0}/screenshot".format(issue.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "screenshot.html")

    def test_show_single_issue_page(self):
        issue = Issue(title="Test Issue")
        issue.save()
        page = self.client.get("/issues/{0}".format(issue.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "issuedetail.html")

    def test_show_single_issue_page_for_issue_that_does_not_exist_(self):
        page = self.client.get("/issues/1")
        self.assertEqual(page.status_code, 404)

    def test_comment_is_added_to_issue(self):
        issue = Issue(title="Test Issue")
        issue.save()
        response = self.client.post("/issues/{0}".format(issue.id),
                                    {"comment": "a test comment"})
        comment = get_object_or_404(Comment)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(comment.comment, "a test comment")

    def test_new_issue_page(self):
        page = self.client.get("/issues/new/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "newissue.html")

    def test_issue_is_created(self):
        response = self.client.post("/issues/new/", {"title": "Test Issue2",
                                    "category": "B", "description": "A Fault"})
        issue = get_object_or_404(Issue)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(issue.title, "Test Issue2")

    def test_voting_function_redirects_issue_bugs(self):
        issue = Issue(title="Test Issue")
        issue.save()
        page = self.client.get("/issues/{0}/voting".format(issue.id))
        self.assertEqual(page.status_code, 302)

    def test_voting_function_redirects_issue_features(self):
        issue = Issue(title="Test Issue", category="F")
        issue.save()
        page = self.client.get("/issues/{0}/voting".format(issue.id))
        self.assertEqual(page.status_code, 302)
