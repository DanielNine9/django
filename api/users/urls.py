from .views import * 
from django.urls import path



urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('active/', ActiveUserApiView.as_view()),
    path('login/', LoginViewSet.as_view()),
    path('reset', ResetPasswordViewSet.as_view()),
]



