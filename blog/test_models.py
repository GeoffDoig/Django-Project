from django.test import TestCase
from .models import Post


class TestPostModel(TestCase):
    def test_post_is_created(self):
        post = Post(title="Test Post", content="words")
        self.assertEqual(post.title, "Test Post")
        self.assertEqual(post.content, "words")
        self.assertEqual(post.views, 0)

    def test_post_as_a_string(self):
        post = Post(title="Test Post")
        self.assertEqual("Test Post", str(post))
