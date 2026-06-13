from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cart, CartItem, Category, CustomUser, Order, OrderItem, Product, ProductRating, Review, Wishlist

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ["username", "email", "first_name", "last_name"]
admin.site.register(CustomUser, CustomUserAdmin)    

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "featured"]
admin.site.register(Product, ProductAdmin)    

class CategorytAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
admin.site.register(Category, CategorytAdmin) 

admin.site.register([Cart, CartItem, Review, ProductRating, Wishlist, Order, OrderItem])
