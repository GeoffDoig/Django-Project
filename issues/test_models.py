from django.test import TestCase
from .models import Issue, Comment


class TestIssueModel(TestCase):
    def test_issue_is_created(self):
        issue = Issue(title="Test Issue", description="Test Description",
                      username="Name")
        self.assertEqual(issue.title, "Test Issue")
        self.assertEqual(issue.description, "Test Description")
        self.assertEqual(issue.username, "Name")
        self.assertEqual(issue.votes, 0)
        self.assertEqual(issue.status, "O")
        self.assertEqual(issue.category, "B")

    def test_issue_as_a_string(self):
        issue = Issue(title="Test Issue")
        self.assertEqual("Test Issue", str(issue))


class TestCommentModel(TestCase):
    def test_comment_is_created_with_id(self):
        comment = Comment(issue_id=1, comment="Test Comment")
        self.assertEqual(comment.issue_id, 1)
        self.assertEqual(comment.comment, "Test Comment")

    def test_comment_username_is_created_with_id(self):
        comment = Comment(issue_id=1, username="Name")
        self.assertEqual(comment.issue_id, 1)
        self.assertEqual(comment.username, "Name")

    def test_comment_as_a_string(self):
        comment = Comment(issue_id=1, username="Name")
        self.assertIn("Name", str(comment))
