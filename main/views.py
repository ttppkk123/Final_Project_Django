from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import ContactMessage, Category, Dish, CartItem
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def booking(request):
    return render(request, 'booking.html')

def contact(request):
    if request.method == 'POST':
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('restaurant:contact')

    return render(request, 'contact.html')

def menu(request):
    categories = Category.objects.all()

    dishes = Dish.objects.all()

    # Filter by spiciness
    spiciness = request.GET.get('spiciness')
    if spiciness == '0':
        dishes = dishes.filter(spiciness=0)

    elif spiciness == '2':
        dishes = dishes.filter(spiciness__in=[1, 2])

    elif spiciness == '3':
        dishes = dishes.filter(spiciness=3)

    elif spiciness == '4':
        dishes = dishes.filter(spiciness__in=[4, 5])

    # Filter by nuts
    nuts = request.GET.get('nuts')
    if nuts == 'true':
        dishes = dishes.filter(nuts=True)
    elif nuts == 'false':
        dishes = dishes.filter(nuts=False)

    # Filter by vegetarian options
    vegetarian = request.GET.get('vegetarian')
    if vegetarian == 'true':
        dishes = dishes.filter(vegetarian=True)
    elif vegetarian == 'false':
        dishes = dishes.filter(vegetarian=False)

    return render(request, 'menu.html', {
        'categories': categories,
        'dishes': dishes,
        'selected_spiciness': spiciness,
        'selected_nuts': nuts,
        'selected_vegetarian': vegetarian,
    })

def add_to_cart(request, dish_id):
    if request.method == 'POST':
        dish = Dish.objects.get(id=dish_id)

        # Create a session if one doesn't exist
        if not request.session.session_key:
            request.session.create()

        session_key = request.session.session_key

        # Check if the dish is already in the cart
        cart_item, created = CartItem.objects.get_or_create(
            dish=dish,
            session_key=session_key,
            defaults={'quantity': 1}
        )

        # If it already exists, increase quantity
        if not created:
            cart_item.quantity += 1
            cart_item.save()

        messages.success(request, f'{dish.name} added to your cart!')

    return redirect('restaurant:menu')

def increase_quantity(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(
            CartItem,
            id=item_id,
            session_key=request.session.session_key
        )

        item.quantity += 1
        item.save()

    return redirect('restaurant:cart')

def decrease_quantity(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(
            CartItem,
            id=item_id,
            session_key=request.session.session_key
        )

        if item.quantity > 1:
            item.quantity -= 1
            item.save()
        else:
            item.delete()

    return redirect('restaurant:cart')

def remove_from_cart(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(
            CartItem,
            id=item_id,
            session_key=request.session.session_key
        )

        item.delete()

    return redirect('restaurant:cart')

def cart(request):
    session_key = request.session.session_key

    cart_items = []
    total_price = 0

    if session_key:
        cart_items = CartItem.objects.filter(
            session_key=session_key
        ).select_related('dish')

        for item in cart_items:
            item.item_total = item.dish.price * item.quantity
            total_price += item.item_total

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })

