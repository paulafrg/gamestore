from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from gamestore.models import Games, Customers, Rents
from gamestore.serializers import GamesSerializer, CustomersSerializer, RentsGamesSerializer, RentsCustomerSerializer
from gamestore.forms import RentForm

def index(request):
    return render(request, 'index.html')

def rent(request):
    form = RentForm()

    if request.method == 'POST':
        form = RentForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Your rent is complete')
            return redirect('index')

    return render(request, 'rent.html', {'form':form})

class GamesViewset(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Games.objects.all()
    serializer_class = GamesSerializer

class CustomersViewset(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer

class ListRentCustomer(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        queryset = Rents.objects.filter(customer_id=self.kwargs['pk'])
        return queryset
    serializer_class = RentsCustomerSerializer

class ListRentGames(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        queryset = Rents.objects.filter(game_id=self.kwargs['pk'])
        return queryset
    serializer_class = RentsGamesSerializer