from django.contrib import admin
from gamestore.models import Games, Customers, Rents

class Game(admin.ModelAdmin):
    list_display = ('id', 'game', 'genre', 'rating',)
    list_display_links = ('id', 'game',)
    list_per_page = 10
    list_filter = ('genre', 'rating',)

admin.site.register(Games, Game)

class Customer(admin.ModelAdmin):
    list_display = ('id', 'name', 'email',)
    list_display_links = ('id', 'name',)
    list_per_page = 10

admin.site.register(Customers, Customer)

class Rent(admin.ModelAdmin):
    list_display = ('id', 'customer', 'game', 'amount',)
    list_display_links = ('id', 'customer',)
    list_per_page = 10

admin.site.register(Rents, Rent)