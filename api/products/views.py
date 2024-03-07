from requests import Response
from rest_framework import viewsets

from common.models import CommonResponse
from .models import *
from .serializers import *
from .permissions import IsSeller
from rest_framework import permissions
from rest_framework import status

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSeller]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSeller]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def create(self, request, *args, **kwargs):
        category_id = request.data.get("category_id")
        if category_id:
            category = Category.objects.filter(pk=category_id).first()
            if category:
                request.data["category"] = category  # Set category field with category object

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return CommonResponse(data = serializer.data, status= status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk:
            product = Product.objects.filter(pk=pk).first()
            if product:
                category_id = request.data.get("category_id")
                if category_id:
                    category = Category.objects.filter(pk=category_id).first()
                    if category:
                        request.data["category"] = category
                        
                
                Product.objects.update(product, data = request.data)
                serializer = self.get_serializer(product)
                serializer.is_valid(raise_exception=True)
                return CommonResponse(data = serializer.data, status=status.HTTP_200_OK, message="Updated product")
        
        return CommonResponse(data = {}, status=status.HTTP_404_NOT_FOUND, message="Product is not found")



    
class ProductItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSeller]
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer

    
class VariationNameViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSeller]
    queryset = VariationName.objects.all()
    serializer_class = VariationNameSerializer

    
class VariationOptionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSeller]
    queryset = VariationOption.objects.all()
    serializer_class = VariationOptionSerializer

