from django.contrib import admin
from .models import *

# Register your models here.
class ProductItemInline(admin.TabularInline):
    model = ProductItem
    extra = 0  # Number of empty forms to display

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductItemInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(VariationName)
admin.site.register(VariationOption)
admin.site.register(Category)