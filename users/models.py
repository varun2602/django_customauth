from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin 

class CustomUserManager(BaseUserManager):
    def create_user(self, email, user_name, password, **other_fields):
        if not user_name:
            raise ValueError('Username is required')
        if not email:
            raise ValueError('Email is required')
        
        email = self.normalize_email(email)
        user = self.model(email = email, user_name = user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email, user_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is False:
            raise ValueError('Superuser should have is_staff set to True')
        if other_fields.get('is_superuser') is False:
            raise ValueError('Superuser should have is_superuser set to True')
        
        return self.create_user(email, user_name, password, **other_fields)
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length = 50, blank = True, null = True, unique = True)
    user_name = models.CharField(max_length = 50, blank = True, null = True)
    password = models.CharField(max_length = 50, blank = True, null = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True) 
    about = models.TextField(max_length = 500, blank = True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.user_name
    
    objects = CustomUserManager()

