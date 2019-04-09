from django.test import TestCase
from .forms import MakePaymentForm, OrderForm


class TestMakePaymentForm(TestCase):
    def test_can_add_card_details(self):
        form = MakePaymentForm({"credit_card_number": "4242",
                                "expiry_month": "5",
                                "expiry_year": "2020",
                                "cvv": "111",
                                "stripe_id": "1"})
        self.assertTrue(form.is_valid())

    def test_correct_message_no_input(self):
        form = MakePaymentForm({"form": ""})
        self.assertFalse(form.is_valid())


class TestOrderForm(TestCase):
    def test_can_add_order_details(self):
        form = OrderForm({"full_name": "Name",
                          "street_address1": "12 Road",
                          "street_address2": "District",
                          "town_or_city": "City",
                          "county": "West",
                          "country": "UK",
                          "phone_number": "0123456789"})
        self.assertTrue(form.is_valid())

    def test_correct_message_no_input(self):
        form = OrderForm({"form": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["full_name"], ["This field is required."])
