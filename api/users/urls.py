from .views import * 
from django.urls import path
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('active/', ActiveUserApiView.as_view()),
]



