from functools import cached_property
from django.db import models
from products.models import ProductItem
from users.models import User

class CartItem(models.Model):
    product = models.ForeignKey(ProductItem, on_delete = models.CASCADE, related_name = "car_items", null = True)
    quantity = models.IntegerField(default = 1)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "cart_items", null = True)
    
    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.order.buyer.get_full_name()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @cached_property
    def cost(self):
        """
        Total cost of the ordered item
        """
        return round(self.quantity * self.product.price, 2)
    
   
