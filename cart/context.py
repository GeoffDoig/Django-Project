from django.shortcuts import get_object_or_404
from issues.models import Issue

def cart_contents(request):
    """ Ensures that the cart contents are available when rendering every page """
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    feature_count = 0
    for pk, quantity in cart.items():
        issue = get_object_or_404(Issue, pk=pk)
        total += quantity * 100
        feature_count += quantity
        cart_items.append({"id": pk, "quantity": quantity, "issue": issue})
    return {"cart_items": cart_items, "total": total, "feature_count": feature_count}