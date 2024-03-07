from django.dispatch import receiver
from django.http import JsonResponse
import requests
from rest_framework import views
from .models import User, ActiveToken, ResetToken
from django.db.models.signals import post_save, pre_save, pre_delete
from .utils import send_email
from .serializers import UserSerializer
from rest_framework import status
from django.utils.translation import gettext_lazy as _
from common.models import CommonResponse
from django.urls import reverse
from rest_framework.permissions import AllowAny



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
    permission_classes = [AllowAny]
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
        base_url = request.build_absolute_uri('/')[:-1]
        request = request.data
        email = request.get("email")
        password = request.get("password")
        if not email or not password:
            return CommonResponse(data = {}, status= status.HTTP_400_BAD_REQUEST, message=_("Email and password are required"))
        response = requests.post(f"{base_url}/api/token/", data={"email": email, "password": password})
        # Check if the request to /api/token was successful
        if response.status_code == status.HTTP_200_OK:
            # Return the response from /api/token
            return CommonResponse(data = response.json(), status=status.HTTP_200_OK)
        else:
            # Return an error response
            return CommonResponse(message = "Email and password are not correct", status=status.HTTP_401_UNAUTHORIZED)
        
class ResetPasswordViewSet(views.APIView):
    def get(self, request):
        email = request.query_params.get("email")
        # token = ResetToken()
        # return CommonResponse(data = {"test": ResetToken.generate_token(token)}, status=status.HTTP_200_OK)
        if email: 
            user = User.objects.filter(email = email).first()
            if not user:
                return CommonResponse(message = _("Email is not found"), status = status.HTTP_404_NOT_FOUND, data = {})
            else: 
                if hasattr(user, 'reset_token'):
                    reset_token = user.reset_token
                    if not reset_token.is_expired():
                        return CommonResponse(message = _("Password reset code sent"), data = {}, status = status.HTTP_204_NO_CONTENT)
                    else:
                        reset_token.token = ResetToken.generate_token()
                else:
                    reset_token = ResetToken(user = user)
                reset_token.save()
                email_subject = 'Reset password'
                email_body = f'Reset password code: '+ str(reset_token.token)
                send_email(email_subject, email_body, email)
                return CommonResponse(message=_("Send mail successfully"), status = status.HTTP_201_CREATED, data= {})
        else:
            return CommonResponse(message = _("Please enter an email"), status= status.HTTP_400_BAD_REQUEST, data = {})
            
    def post(self, request):
        email = request.query_params.get("email")
        token = request.query_params.get("token")
        password = request.data.get("password")

        if email and token and password.strip():
            user = User.objects.filter(email=email).first()
            if not user:
                return CommonResponse(message=_("Email is not found"), data={}, status=status.HTTP_404_NOT_FOUND)
            
            if hasattr(user, 'reset_token'):
                reset_token = user.reset_token
                if reset_token is not None and not reset_token.is_expired():
                    if reset_token.token == token:
                        user.set_password(password)
                        user.save()
                        return CommonResponse(message=_("Change password successfully " + str(password)), data={}, status=status.HTTP_204_NO_CONTENT)
                else:
                    return CommonResponse(message=_("This token is expired"), status=status.HTTP_400_BAD_REQUEST)
            
            return CommonResponse(message=_("This token is not valid"), status=status.HTTP_400_BAD_REQUEST)
        else:
            return CommonResponse(message=_("Email, reset token, password are required"), status=status.HTTP_400_BAD_REQUEST, data={})

            
   
        

       
        
        
       
