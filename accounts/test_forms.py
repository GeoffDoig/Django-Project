from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm, ProfileUpdateForm


class TestUserLoginForm(TestCase):
    def test_can_login(self):
        form = UserLoginForm({"username": "name", "password": "secret"})
        self.assertTrue(form.is_valid())

    def test_correct_message_no_input(self):
        form = UserLoginForm({"form": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["username"], ["This field is required."])


class TestUserRegistrationForm(TestCase):
    def test_can_register_user(self):
        form = UserRegistrationForm({"username": "name",
                                     "email": "name@mail.com",
                                     "password1": "secret",
                                     "password2": "secret"})
        self.assertTrue(form.is_valid())

    def test_correct_message_no_input(self):
        form = UserRegistrationForm({"form": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["username"], ["This field is required."])


class TestProfileUpdateForm(TestCase):
    def test_can_create_profile(self):
        form = ProfileUpdateForm({"full_name": "Name2",
                                  "street_address1": "12 Road",
                                  "street_address2": "District",
                                  "town_or_city": "City",
                                  "county": "West",
                                  "country": "UK",
                                  "phone_number": "0123456789"})
        self.assertTrue(form.is_valid())
