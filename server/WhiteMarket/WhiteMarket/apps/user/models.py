from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models

# Create your models here.

class UserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, we get a lot of the same code used by
    Django to create a `User` for free. 
    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """


    def create_user(self, username, email,latitude, longitude, password=None):

        print(latitude)
        print(longitude)
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email address.')
        if latitude is None:
            raise TypeError('Users must have an latitude address.')
        if longitude is None:
            raise TypeError('Users must have an longitude address.')

        user = self.model(username=username, email=self.normalize_email(email), latitude=latitude, longitude=longitude)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, latitude, longitude, password):

        user = self.model(username=username, email=self.normalize_email(email), latitude=latitude, longitude=longitude)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin ):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','latitude','longitude']
    objects = UserManager()