from rest_framework import serializers
from .models import CartItem
from products.serializers import ProductItemSerializer

class CartSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    cost = serializers.SerializerMethodField()
    
    def get_product(self, cart):
        if cart.product:
            return ProductItemSerializer(cart.product).data
        return None
    
    def get_cost(self, cart):
        if cart:
            return cart.cost()
        return 0
 
    class Meta:
        model = CartItem
        fields = "__all__"