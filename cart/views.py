from django.shortcuts import render, redirect

# Create your views here.

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
