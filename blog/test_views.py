from django.test import TestCase
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Post


class TestBlogViews(TestCase):
    def test_show_posts_page(self):
        page = self.client.get("/blog/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blogposts.html")

    def test_show_single_post_page(self):
        user = User(username="Name2")
        user.save()
        post = Post(title="Test Post", author=user)
        post.save()
        page = self.client.get("/blog/{0}".format(post.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "postdetail.html")

    def test_new_post_page(self):
        user = User(username="Name")
        user.save()
        self.client.force_login(user)
        page = self.client.get("/blog/new/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blogpostform.html")

    def test_post_is_created(self):
        user = User(username="Name")
        user.save()
        self.client.force_login(user)
        response = self.client.post("/blog/new/", {"title": "Test Post2",
                                    "author": user, "content": "Words"})
        post = get_object_or_404(Post)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(post.title, "Test Post2")
