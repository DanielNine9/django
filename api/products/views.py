from rest_framework import viewsets
from .models import *
from .serializers import *
from .permissions import *

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSeller]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSeller]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
        
    
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
