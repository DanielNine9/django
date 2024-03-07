from datetime import datetime, timedelta
from django.utils import timezone
import random
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

    
class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, is_active = False, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        if not password:
            raise ValueError(_("The passwrod must be set"))
        if User.objects.filter(email=email).exists(): 
            raise ValueError(_("Email is already taken"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_active = is_active
        user.save()
        
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)    
    

class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="users/%Y/%m")
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    
class Token(models.Model):
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    expires_at = models.DateTimeField(_("expires at"))
    @staticmethod
    def generate_token():
        """
        Generate a random active token.
        """
        return random.randint(100000, 999999)
  
    def is_expired(self):
        """
        Check if the token has expired.
        """
        return self.expires_at < timezone.now()
    class Meta: 
        abstract = True
    
class ActiveToken(Token):
    token = models.CharField(_("active token"), max_length=50, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="active_token")
    
    def save(self, *args, **kwargs):
        print(args)
        print(kwargs)
        self.token = self.generate_token()
        self.expires_at = datetime.now() + timedelta(minutes=10)  
        return super().save(*args, **kwargs)

class ResetToken(Token):
    token = models.CharField(_("reset token"), max_length=50, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="reset_token")
    
    def save(self, *args, **kwargs):
        self.token = Token.generate_token()
        self.expires_at = datetime.now() + timedelta(minutes=10)  
        return super().save(*args, **kwargs)

   

   