from django import forms
from .models import Order


class MakePaymentForm(forms.Form):
    MONTH_CHOICE = [(i, i) for i in range(1, 13)]
    YEAR_CHOICE = [(i, i) for i in range(2017, 2036)]

    credit_card_number = forms.CharField(label="Credit Card Number",
                                         required=False)
    expiry_month = forms.ChoiceField(label="Expiry Month",
                                     choices=MONTH_CHOICE, required=False)
    expiry_year = forms.ChoiceField(label="Expiry Year",
                                    choices=YEAR_CHOICE, required=False)
    cvv = forms.CharField(label="Security Code (CVV)", required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["full_name", "street_address1", "street_address2",
                  "town_or_city", "county", "country", "postcode",
                  "phone_number"]
