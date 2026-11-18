from django.http import JsonResponse
from main.models import Category, Dish, CartItem, ContactMessage

# Gets all products from the database
def api_get_all_products(request):
    dishes = Dish.objects.select_related('category').all()

    data = []

    for dish in dishes:
        data.append({
            'id': dish.id,
            'name': dish.name,
            'description': dish.description,
            'price': str(dish.price),
            'category': dish.category.name,
            'spiciness': dish.spiciness,
            'nuts': dish.nuts,
            'vegetarian': dish.vegetarian,
        })

    return JsonResponse(data, safe=False)

# Filters products based on the parameters provided in the URL
def api_get_filtered_products(request):
    dishes = Dish.objects.select_related('category').all()

    vegetarian = request.GET.get('vegetarian')
    nuts = request.GET.get('nuts')
    spiciness = request.GET.get('spiciness')

    if vegetarian is not None:
        dishes = dishes.filter(vegetarian=vegetarian.lower() == 'true')

    if nuts is not None:
        dishes = dishes.filter(nuts=nuts.lower() == 'true')

    if spiciness is not None:
        dishes = dishes.filter(spiciness=int(spiciness))
       
    data = []

    for dish in dishes:
        data.append({
            'id': dish.id,
            'name': dish.name,
            'description': dish.description,
            'price': str(dish.price),
            'category': dish.category.name,
            'spiciness': dish.spiciness,
            'nuts': dish.nuts,
            'vegetarian': dish.vegetarian,
        })

    return JsonResponse(data, safe=False)


# Gets all categories from the database
def api_get_all_categories(request):
    categories = Category.objects.all().values()

    return JsonResponse(list(categories), safe=False)

# Gets one specific category using ID
def api_get_category(request, id):
    category = Category.objects.get(id=id)

    data = {
        'id': category.id,
        'name': category.name,
    }
    return JsonResponse(data)

# Gets the current session key or create new if visitor does not have one
def get_cart_session_key(request):
    if not request.session.session_key:
        request.session.create()

    return request.session.session_key


# Get all items in the basket.
def api_get_all_basket_items(request):
    session_key = get_cart_session_key(request)

    cart_items = CartItem.objects.filter(
        session_key=session_key
    ).select_related('dish')

    data = []

    for item in cart_items:
        data.append({
            'id': item.id,
            'dish_id': item.dish.id,
            'dish_name': item.dish.name,
            'price': str(item.dish.price),
            'quantity': item.quantity,
            'total': str(item.dish.price * item.quantity),
        })

    return JsonResponse(data, safe=False)

# Delete item from the basket
def api_delete_basket_product(request, id):
    session_key = get_cart_session_key(request)

    cart_item = CartItem.objects.get(
        id=id,
        session_key=session_key
    )
    
    cart_item.delete()

    return JsonResponse({'message': 'Product removed from basket'})

# Gets all messages
def api_get_all_messages(request):
    messages = ContactMessage.objects.all().values()

    return JsonResponse(list(messages), safe=False)
