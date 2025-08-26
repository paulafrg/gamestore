from rest_framework import serializers
from gamestore.models import Games, Customers, Rents

class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = "__all__"

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = "__all__"

class RentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rents
        fields = "__all__"

class RentsCustomerSerializer(serializers.ModelSerializer):
    game = serializers.ReadOnlyField(source='game.game')
    amount = serializers.SerializerMethodField()
    class Meta:
        model = Rents
        fields = ['game', 'amount']
    def get_amount(self, obj):
        return obj.amount
    
class RentsGamesSerializer(serializers.ModelSerializer):
    customer = serializers.ReadOnlyField(source='customer.name')
    amount = serializers.SerializerMethodField()
    class Meta:
        model = Rents
        fields = ['customer', 'amount']
    def get_amount(self, obj):
        return obj.amount