from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils import timezone


class UserAuthManager(BaseUserManager):
    
    def create_user(self, email, username, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        
        email=self.normalize_email(email)
        user = self.model(
            email = email,
            username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email,username, password):
        """
        Creates and saves a superuser with the given email and
        password.
        """
        if password is None:
            raise ValueError("super user must have a password.")
        user = self.create_user(
            email = email,
            username = username,
            password=password,
        )
        
        user.is_admin = True
        user.save(using=self._db)
        return user
    
    
class UserAuth(AbstractBaseUser):
    
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    username = models.CharField(max_length = 50, unique = True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = UserAuthManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def get_full_name(self):
        return self.username
    
    def __str__(self):
        return self.email
    
