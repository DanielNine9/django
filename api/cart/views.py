from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CartSerializer
from .models import CartItem
from common.models import CommonResponse
from rest_framework import status
from users.models import User
from django.utils.translation import gettext as _
from rest_framework.permissions import IsAuthenticated
from products.models import ProductItem

# Create your views here.


class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    queryset = CartItem.objects.all()
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = User.objects.filter(pk=self.request.user.id).first()
        if user:
            return user.cart_items.all()  # Assuming `cart_items` is a related name for the cart items queryset
        else:
            return CartItem.objects.none()  # Return an empty queryset if the user is not found

    def list(self, request, *args, **kwargs):
        serializers = self.get_serializer(self.get_queryset(), many=True)
        return CommonResponse(data=serializers.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if not serializer.is_valid():
            return CommonResponse(message = _("Adding cart failed"), status= status.HTTP_400_BAD_REQUEST, errors = serializer.errors)
        
        product_id = request.data.get("product")
        if product_id is None:
            return CommonResponse(message = _("Product is not found"), status = status.HTTP_404_NOT_FOUND)
        
        try:
            product = ProductItem.objects.get(pk = product_id)
        except Exception: 
            return CommonResponse(message = _("Product is not found"), status = status.HTTP_404_NOT_FOUND)
            
        cart_item = serializer.save()
        cart_item.user = request.user
        cart_item.product = product
        
        cart_item.save()
        return CommonResponse(data = serializer.data, status = status.HTTP_201_CREATED)
    

    def retrieve(self, request, *args, **kwargs):
        try:
            cart_item = self.get_object()
        except Exception:
            return CommonResponse(
                status=status.HTTP_404_NOT_FOUND, message=_("Cart item is not found")
            )
        serializer = self.get_serializer(cart_item)
        return CommonResponse(data=serializer.data)

    def update(self, request, *args, **kwargs):
        try:
            cart_item = self.get_object()
        except Exception:
            return CommonResponse(
                status=status.HTTP_404_NOT_FOUND, message=_("Cart item is not found")
            )
        quantity_in_stock = cart_item.product.quantity_in_stock
        if (quantity_in_stock - request.data.get("quantity")) < 0:
            return CommonResponse(status = status.HTTP_400_BAD_REQUEST, message = _("Quantity greater than quantity in stock"))
        serializer = self.get_serializer(cart_item, data=request.data)
        if not serializer.is_valid():
            return CommonResponse(
                status=status.HTTP_400_BAD_REQUEST,
                message="Updating cart item failed",
                erros=serializer.errors,
            )
        self.perform_update(serializer)
        return CommonResponse(data = serializer.data, message = "Updating cart item successfully")

    def destroy(self, request, *args, **kwargs):
        try:
            cart_item = self.get_object()
        except Exception:
            return CommonResponse(
                status=status.HTTP_404_NOT_FOUND, message=_("Cart item is not found")
            )

        self.perform_destroy(cart_item)
        return CommonResponse(
            status=status.HTTP_204_NO_CONTENT, message="Cart item deleted"
        )
