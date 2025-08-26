from django.urls import path
from gamestore.views import index, rent

urlpatterns = [
    path('', index, name='index'),
    path('rent', rent, name='rent'),
]
