from datetime import timezone
from django.db import models
from django.utils.translation import gettext as _

class BaseModel(models.Model):
    created_at = models.DateTimeField( auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default = True)
    class Meta:
        abstract= True
     
class Category(BaseModel):
    name = models.CharField(max_length=100, unique = True)
    image = models.ImageField(upload_to="category/%Y/%m", default="category/default")
    def __str__(self):
        return str(self.name)

class Product(BaseModel):
    name = models.CharField(max_length=123, null=True)
    image = models.ImageField(upload_to="product/%Y/%m", default="product/default.png")
    description = models.TextField(null=True, blank=True)
    discount = models.FloatField(default = 0)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE, null=True)
    
    class Meta: 
        unique_together = ("name", "category")
        
    def __str__(self): 
        if self.category:
            return self.name + " in category " + self.category.name
        return self.name
     
class ProductItem(BaseModel):
    variation_options = models.ManyToManyField('VariationOption', related_name="products", default = [])
    product = models.ForeignKey(Product, related_name = "product_items", on_delete = models.CASCADE, null = True)
    quantity = models.IntegerField(default = 0)
    price = models.FloatField(default = 0)
    def __str__(self):
        return "item " + self.product.name
    
class VariationName(models.Model):
    name = models.CharField(max_length = 100, default= _("Default variation name"))
    category = models.ForeignKey(Category, related_name = "variation_names", on_delete = models.CASCADE, null = True)
    class Meta:
        unique_together = ("name", "category")
        
    def __str__(self):
        return self.name
    
class VariationOption(models.Model): 
    value = models.CharField(max_length= 100, default = _("Default variation option"))
    variation_name = models.ForeignKey(VariationName, related_name = "variation_options", on_delete = models.CASCADE, null = True)
    class Meta:
        unique_together = ("value", "variation_name")
    
    def __str__(self):
        return self.value + " is option of " + self.variation_name.name
        