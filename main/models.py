from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta: 
        db_table = 'Categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.URLField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="dishes")
    spiciness = models.IntegerField(default=0)
    nuts = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)

    class Meta: 
        db_table = 'Dishes'
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'

    def __str__(self):
        return self.name


class CartItem(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name="cart_items")
    quantity = models.PositiveIntegerField(default=1)
    session_key = models.CharField(max_length=40)

    class Meta: 
        db_table = 'CartItems'

    def __str__(self):
        return f"{self.dish.name} x {self.quantity}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Messages'

    def __str__(self):
        return f"{self.subject}"

