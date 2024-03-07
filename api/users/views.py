from django.dispatch import receiver
from django.http import JsonResponse
from rest_framework import views
from .models import User, ActiveToken
from django.db.models.signals import post_save, pre_save, pre_delete
from .utils import send_email
from .serializers import UserSerializer
from rest_framework import status
from django.utils.translation import gettext_lazy as _
from common.models import CommonResponse



@receiver(post_save, sender=User) 
def create_profile(sender, instance, created, **kwargs):
    if created:
        active_token = ActiveToken(user = instance)
        active_token.save()
        # Assuming you want to pass some user-related information to the send_email function
        email_subject = 'Welcome to Our Website'
        email_body = f'code is: '+ str(active_token.token)
        
        # Pass the necessary information to the send_email function
        send_email(email_subject, email_body, instance.email)


class RegisterApiView(views.APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if email and password:
            user_serializer = UserSerializer(data=request.data)
            if user_serializer.is_valid():
                user = user_serializer.save()  # Save the user instance
                return CommonResponse(data=user_serializer.data, status=status.HTTP_201_CREATED, message="User created successfully")
            else:
                return CommonResponse(errors=user_serializer.errors, status=status.HTTP_400_BAD_REQUEST, message="Validation errors")
        else:
            return CommonResponse(data={"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST, message="Invalid request data")
        
class ActiveUserApiView(views.APIView):
    def post(self, request):
        email = request.data.get("email")
        token = request.data.get("token")
        if email and token:
            try:
                user = User.objects.get(email=email)
                if user.is_active:
                    return CommonResponse(data = {}, status= status.HTTP_200_OK, message=_("This account is actived"))
                active_token = user.active_token
                if active_token.is_expired():
                    return CommonResponse(data={}, status=status.HTTP_400_BAD_REQUEST, message=_("Token is expired"))
                if active_token.token == token:
                    user.is_active = True
                    user.save()
                    return CommonResponse(data={}, status=status.HTTP_200_OK, message=_("User activated successfully"))
                else:
                    return CommonResponse(data={}, status=status.HTTP_400_BAD_REQUEST, message=_("Invalid token"))
            except User.DoesNotExist:
                return CommonResponse(data={}, status=status.HTTP_400_BAD_REQUEST, message=_("User with this email does not exist"))
        return CommonResponse(data={}, status=status.HTTP_400_BAD_REQUEST, message="Invalid request data")
    
class LoginViewSet(views.APIView):
    def post(self, request):
        request = request.data
        email = request.get("email")
        password = request.get("password")
        if not email or not password:
            return CommonResponse(data = {}, status= status.HTTP_400_BAD_REQUEST, message=_("Email and password are required"))
        
        

       
        
        
       
