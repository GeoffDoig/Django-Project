from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from .models import OrderLineItem
from .forms import OrderForm, MakePaymentForm
from issues.models import Issue
import stripe


stripe.api_key = settings.STRIPE_SECRET


def checkout(request):
    """ Display order and payment forms and process payment """
    user = User.objects.get(email=request.user.email)
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            cart = request.session.get("cart", {})
            total = 0
            for id, quantity in cart.items():
                issue = get_object_or_404(Issue, pk=id)
                total += quantity * 100
                order_line_item = OrderLineItem(order=order, issue=issue,
                                                quantity=quantity)
                order_line_item.save()
            try:
                customer = stripe.Charge.create(amount=int(total * 100),
                                                currency="GBP",
                                                description=request.user.email,
                                                card=payment_form.cleaned_data
                                                ["stripe_id"])
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            if customer.paid:
                messages.success(request,
                                 "Thank You! Your payment was successful!")
                request.session["cart"] = {}
                return redirect("issues")
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request,
                           "We are unable to take a payment with that card")
    else:
        order_form = OrderForm(instance=user.userprofile)
        payment_form = MakePaymentForm()
    return render(request, "checkout.html", {"order_form": order_form,
                                             "payment_form": payment_form,
                                             "publishable":
                                                 settings.STRIPE_PUBLISHABLE})
