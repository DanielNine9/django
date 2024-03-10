from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cart', CartItemViewSet, basename='cart_item')

urlpatterns = router.urls

