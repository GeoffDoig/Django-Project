from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile


class TestUserProfileModel(TestCase):
    def test_userprofile_is_created(self):
        profile = UserProfile(user_id=1,
                              full_name="Name2",
                              street_address1="12 Road",
                              street_address2="District",
                              town_or_city="City",
                              county="West",
                              country="UK",
                              phone_number="0123456789")
        profile.save()
        self.assertEqual(profile.full_name, "Name2")
        self.assertEqual(profile.street_address1, "12 Road")
        self.assertEqual(profile.street_address2, "District")
        self.assertEqual(profile.town_or_city, "City")
        self.assertEqual(profile.county, "West")
        self.assertEqual(profile.country, "UK")
        self.assertEqual(profile.phone_number, "0123456789")

    def test_userprofile_as_a_string(self):
        user = User(username="Test")
        user.save()
        profile = UserProfile(user=user)
        self.assertEqual("Test", str(profile))
