from django.test import TestCase
from .forms import BlogPostForm


class TestBlogPostForm(TestCase):
    def test_can_create_post(self):
        form = BlogPostForm({"title": "test post",
                             "content": "some text",
                             "tag": "test"})
        self.assertTrue(form.is_valid())

    def test_correct_message_no_input(self):
        form = BlogPostForm({"form": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["title"], ["This field is required."])
