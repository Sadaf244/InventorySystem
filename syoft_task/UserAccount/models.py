from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

    
class UserModel(AbstractUser):
    username=models.CharField(max_length=150,null=False, blank=False)
    phone=PhoneNumberField()
    email=models.EmailField(blank=False, null=False,unique=True)
    password=models.CharField(max_length=150,null=False, blank=False)
    ROLE_CHOICES=(
        ('Admin','Admin'),
        ('Manager','Manager'),
        ('Staff','Staff'),
    )
    role=models.CharField(max_length=200,blank=False,null=False, choices=ROLE_CHOICES)
    
    USERNAME_FIELD="email"
    REQUIRED_FIELDS = []
    PHONE_FIELD="phone"
    NAME_FIELD="username"
    PASSWORD_FIELD="password"
    ROLE_FIELD="role"
    

