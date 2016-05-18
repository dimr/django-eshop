from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Cart, CartItem
from django.core.urlresolvers import reverse
from products.models import Product


# Create your views here.



def view(request):
    try:
        the_id = request.session['cart_id']
    except:
        the_id = None
    if the_id:
        cart = Cart.objects.get(id=the_id)
        context = {"cart": cart}
    else:
        message = "you cart is empty"
        context = {"empty": True, "message": message}
    template = "view_cart.html"
    return render(request, template, context)


def update_cart(request, slug):
    request.session.set_expiry(10)
    try:
        qty = request.POST.get('qty', '')
        print(qty)
        update_qty = True
    except:
        qty = ''
        update_qty = False

    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id
    cart = Cart.objects.get(id=the_id)
    if request.method == "POST":
        print("POST request CART", request.POST)
        print(request.POST.get('qty'))
    print(request)
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if update_qty and qty:
        if int(qty) == 0:
            cart_item.delete()
        else:
            cart_item.quantity = qty
            cart_item.save()
    else:
        pass

    new_total = 0.00
    for item in cart.cartitem_set.all():
        line_total = float(item.product.price) * float(item.product.price)
        new_total += float(item.product.price)
    request.session['items_total'] = cart.cartitem_set.count()
    cart.total = new_total
    cart.save()
    return HttpResponseRedirect(reverse("cart"))
