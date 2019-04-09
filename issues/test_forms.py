from django.test import TestCase
from .forms import CommentsForm, NewIssueForm


class TestCommentsForm(TestCase):
    def test_can_add_comment(self):
        form = CommentsForm({"comment": "test comment"})
        self.assertTrue(form.is_valid())

    def test_correct_message_no_input(self):
        form = CommentsForm({"form": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["comment"], ["This field is required."])


class TestNewIssueForm(TestCase):
    def test_can_create_issue(self):
        form = NewIssueForm({"title": "test issue",
                             "description": "some text",
                             "category": "B"})
        self.assertTrue(form.is_valid())

    def test_correct_message_no_input(self):
        form = NewIssueForm({"form": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["title"], ["This field is required."])
