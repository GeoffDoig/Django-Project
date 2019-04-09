from django.test import TestCase
from .models import Order, OrderLineItem
from issues.models import Issue


class TestOrderModel(TestCase):
    def test_order_is_created(self):
        order = Order(full_name="Name",
                      street_address1="12 Road",
                      street_address2="District",
                      town_or_city="City",
                      county="West",
                      country="UK",
                      phone_number="0123456789",
                      date="2019-04-08")
        order.save()
        self.assertEqual(order.full_name, "Name")
        self.assertEqual(order.street_address1, "12 Road")
        self.assertEqual(order.street_address2, "District")
        self.assertEqual(order.town_or_city, "City")
        self.assertEqual(order.county, "West")
        self.assertEqual(order.country, "UK")
        self.assertEqual(order.phone_number, "0123456789")

    def test_order_as_a_string(self):
        order = Order(full_name="Name", date="2019-04-08")
        order.save()
        self.assertIn("Name", str(order))


class TestOrderLineItemModel(TestCase):
    def setUp(self):
        order = Order(full_name="Name", date="2019-04-08")
        order.save()
        issue = Issue(title="Test Issue")
        issue.save()

    def test_order_item_is_created(self):
        item = OrderLineItem(quantity=1, issue_id=1, order_id=1)
        item.save()
        self.assertEqual(item.order.full_name, "Name")
        self.assertEqual(item.issue.title, "Test Issue")
        self.assertEqual(item.quantity, 1)

    def test_order_line_item_as_a_string(self):
        item = OrderLineItem(quantity=1, issue_id=1, order_id=1)
        item.save()
        self.assertIn("Name", str(item))
