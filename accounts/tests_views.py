from django.test import TestCase
from django.contrib.auth.models import User


class TestAccountsViews(TestCase):
    def test_show_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")

    def test_show_login_page(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")

    def test_show_registration_page(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")

    def test_show_profile_page(self):
        user = User(username="Name")
        user.save()
        self.client.force_login(user)
        page = self.client.get("/accounts/profile/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")

    def test_profile_is_updated(self):
        user = User(username="Name")
        user.save()
        self.client.force_login(user)
        response = self.client.post("/accounts/profile/",
                                    {"full_name": "Name2",
                                     "street_address1": "12 Road",
                                     "street_address2": "District",
                                     "town_or_city": "City",
                                     "county": "West",
                                     "country": "UK",
                                     "phone_number": "0123456789"})
        self.assertEqual(response.status_code, 302)

    def test_logout(self):
        page = self.client.get("/accounts/logout/")
        self.assertEqual(page.status_code, 302)
