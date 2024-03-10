from rest_framework import serializers

from common.models import CommonResponse
from rest_framework import status
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    
    def get_products(self, obj):
        return ProductInCategorySerializer(obj.products, many = True).data
    class Meta:
        model = Category
        fields = "__all__"
        
class CategoryUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]



class ProductInCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['category']

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    product_items = serializers.SerializerMethodField()

    def get_category(self, obj):
        if obj.category:
            return {"name": obj.category.name, "id": obj.category.id}
        return None

    def get_product_items(self, obj):
        product_items_queryset = (
            obj.product_items.all()
        )  # Retrieve related product items
        product_items_serializer = ProductItemSerializer(
            product_items_queryset, many=True, context=self.context
        )
        return product_items_serializer.data

    class Meta:
        model = Product
        fields = "__all__"


class ProductItemSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    variation_options = serializers.SerializerMethodField()

    def get_variation_options(self, obj):
        variation_options = {}
        for option in obj.variation_options.all():
            variation_name = option.variation_name.name
            value = {option.value}
            variation_options.setdefault(variation_name, []).append(value)
        return variation_options

    def get_product(self, obj):
        if obj.product:
            product = obj.product
            return {"name": product.name, "id": product.id}
        return None

    class Meta:
        model = ProductItem
        fields = "__all__"


class VariationNameSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    variation_options = serializers.SerializerMethodField()

    def get_category(self, obj):
        if obj.category:
            return {"name": obj.category.name}
        return None

    def get_variation_options(self, obj):
        variation_options = VariationOption.objects.filter(variation_name=obj)
        # Apply the map function over the variation_options queryset
        mapped_values = map(lambda option: {"value": option.value}, variation_options)
        # Convert the mapped values to a list (if needed)
        mapped_values_list = list(mapped_values)
        return mapped_values_list

    class Meta:
        model = VariationName
        fields = "__all__"


class VariationOptionSerializer(serializers.ModelSerializer):
    product_items = serializers.SerializerMethodField()
    variation_name = serializers.SerializerMethodField()

    def get_product_items(self, obj):
        product_item_serializer = ProductItemSerializer(
            obj.products.all(), many=True
        )
        return product_item_serializer.data

    def get_variation_name(self, obj):
        if obj.variation_name:
            return {
                "id": obj.variation_name.id,
                "variation_name": obj.variation_name.name,
                }  # Assuming 'variation_name' has a 'name' attribute
        return None

    class Meta:
        model = VariationOption 
        fields = "__all__"
