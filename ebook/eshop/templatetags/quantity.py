from django import template
from eshop.models import Cart

register = template.Library()

@register.filter
def products_in_cart(user):
    if user.is_authenticated:
        cart = Cart.objects.filter(UserID=user)
        if cart.exists():
            return cart[0].TotalQuantity
    return 0
