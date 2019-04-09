from django.test import TestCase
from django.contrib.auth.models import User


class TestCheckoutViews(TestCase):
    def setUp(self):
        user = User(username="Name")
        user.save()
        self.client.force_login(user)

    def test_show_checkout_page(self):
        page = self.client.get("/checkout/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "checkout.html")
