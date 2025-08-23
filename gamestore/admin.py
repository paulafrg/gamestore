from django.contrib import admin
from gamestore.models import Games, Customers

class Game(admin.ModelAdmin):
    list_display = ('id', 'game', 'genre', 'rating',)
    list_display_links = ('id', 'game',)
    list_per_page = 10
    list_filter = ('genre', 'rating',)

admin.site.register(Games, Game)