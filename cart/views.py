from django.shortcuts import render, redirect, get_object_or_404
from issues.models import Issue


def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, pk):
    """ Add one to cart for specified feature requested """
    quantity = 1
    cart = request.session.get("cart", {})
    cart[pk] = cart.get(pk, quantity)
    request.session["cart"] = cart
    return redirect("show_issue", pk=pk)


def adjust_cart(request, pk):
    """ Remove the request for a feature to be developed """
    issue = get_object_or_404(Issue, pk=pk)
    cart = request.session.get("cart", {})
    cart.pop(pk)
    issue.votes -= 1
    issue.save()
    request.session["cart"] = cart
    return redirect("view_cart")
