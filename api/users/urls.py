from .views import * 
from django.urls import path

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'address', AddressViewSet, basename='address')
router.register(r'profile', ProfileViewSet, basename= 'profile')

url_address = router.urls

urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('active/', ActiveUserApiView.as_view()),
    path('login/', LoginViewSet.as_view()),
    path('reset', ResetPasswordViewSet.as_view()),
] + url_address



