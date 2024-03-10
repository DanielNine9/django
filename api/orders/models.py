from functools import cached_property
from django.db import models
from django.utils.translation import gettext as _
from users.models import User, Address
from products.models import ProductItem

# Create your models here.

class Order(models.Model):
    PENDING = "P"
    COMPLETED = "C"
    BILLING = "B"
    SHIPPING = "S"
    
    ADDRESS_CHOICES = ((BILLING, _("billing")), (SHIPPING, _("shipping")))
    STATUS_CHOICES = ((PENDING, _("pending")), (COMPLETED, _("completed")))
    
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES, null = True, blank = True)
    buyer = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PENDING)
    address = models.ForeignKey(Address, related_name = "orders", on_delete = models.SET_NULL, null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.buyer.get_full_name()

    @cached_property
    def total_cost(self):
        """
        Total cost of all the items in an order
        """
        return round(sum([order_item.cost for order_item in self.order_items.all()]), 2)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name="order_items", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        ProductItem, related_name="product_orders", on_delete=models.CASCADE
    )
    quantity = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.order.buyer.get_full_name()

    @cached_property
    def cost(self):
        """
        Total cost of the ordered item
        """
        return round(self.quantity * self.product.price, 2)

    