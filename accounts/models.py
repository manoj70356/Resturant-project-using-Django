from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
# Create your models here.

class MyAccountManager(BaseUserManager):
  def create_user(self, email, password = None):
    if not email:
      raise ValueError("Email Required")
    
    user = self.model(email=self.normalize_email(email))
    user.set_password(password)
    user.is_active = True
    user.save(using=self._db)
    return user
  

  def create_superuser(self, email, password):
    user = self.create_user(email, password)
    user.is_staff = True
    user.is_superuser = True
    user.save(using=self._db)
    return user
  
class Account(AbstractBaseUser,PermissionsMixin):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField(unique=True)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=True)  
  date_joined = models.DateTimeField(auto_now_add=True)


  objects = MyAccountManager()
  USERNAME_FIELD = 'email'


  def __str__(self):
    return self.email