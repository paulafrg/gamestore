from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from gamestore.views import GamesViewset, CustomersViewset, ListRentCustomer, ListRentGames

router = routers.DefaultRouter()
router.register('games', GamesViewset, basename='games')
router.register('customers', CustomersViewset, basename='customers')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/customers/<int:pk>/rents/', ListRentCustomer.as_view()),
    path('api/games/<int:pk>/rents/', ListRentGames.as_view()),
    path('', include('gamestore.urls'))
]
