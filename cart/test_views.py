from django.test import TestCase
from issues.models import Issue


class TestCartViews(TestCase):
    def test_show_cart_page(self):
        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart.html")

    def test_add_to_cart(self):
        issue = Issue(title="Test Issue")
        issue.save()
        page = self.client.get("/cart/add/{0}".format(issue.id))
        self.assertEqual(page.status_code, 302)
