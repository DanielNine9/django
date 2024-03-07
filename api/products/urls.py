from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')
router.register(r'product-item', ProductItemViewSet, basename='product_item')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'variation-name', VariationNameViewSet, basename='variation_name')
router.register(r'variation-option', VariationOptionViewSet, basename='variation_option')
urlpatterns = router.urls

