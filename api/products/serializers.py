from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

 
        
class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    
    def get_category(self, obj):
        if obj.category:
            category_serializer = CategorySerializer(obj.category, context=self.context)
            return category_serializer.data
        return None
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.product_items.exists():
            representation['product_items'] = ProductItemSerializer(instance.product_items.all(), many=True).data
        return representation
    
    class Meta:
        model = Product
        fields  = "__all__"
        
class ProductItemSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    variation_option = serializers.SerializerMethodField()

    def get_variation_option(self, obj):
        variation_option_queryset = obj.variation_options.all()
        if variation_option_queryset.exists():
            variation_options_serializer = VariationOptionSerializer(variation_option_queryset, many=True)
            return variation_options_serializer.data
        return []

    def get_product(self, obj):
        if obj.product:
            return ProductSerializer(obj.product).data
        return None

    class Meta:
        model = ProductItem
        fields = '__all__'
        
class VariationNameSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    
    def get_category(self, obj):
        if obj.category:
            return CategorySerializer(obj.category).data
        return None
    
    class Meta:
        model = VariationName
        fields = '__all__'

    
class VariationOptionSerializer(serializers.ModelSerializer):
    product_items = serializers.SerializerMethodField()
    variation_name = serializers.SerializerMethodField()
    
    def get_product_items(self, obj): 
        product_items_queryset = obj.product_items.all() 
        print(obj.product_items)
        if product_items_queryset.exists():
            product_item_serializer = ProductItemSerializer(product_items_queryset, many=True)
            return product_item_serializer.data
        return []
    
    def get_variation_name(self, obj):
        if obj.variation_name: 
            return VariationName(obj.variation_name).data
        return None

    class Meta:
        model = VariationOption
        fields = '__all__'