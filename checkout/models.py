from django.db import models
from issues.models import Issue


class Order(models.Model):
    """
    Fields required for user order and invoice
    """
    full_name = models.CharField(max_length=50, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    phone_number = models.CharField(max_length=20, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    """
    Fields required to place an order for a specific issue
    """
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.order.full_name,
                                    self.issue.title)
