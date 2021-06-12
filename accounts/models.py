from django.contrib.auth.models import AbstractBaseUser
from django.db import models

# Create your models here.
# class CustomUser(AbstractBaseUser):
# 		#email = models.CharField(max_length=40, unique=True)
# 		USERNAME_FIELD = 'email'
# 		REQUIRED_FIELDS = ['email']
#
# 		def natural_key(self):
# 				return dict(email=self.email)
#
#
# CustomUser._meta.get_field('email')._unique = True
# CustomUser._meta.get_field('email')._blank = False
# CustomUser._meta.get_field('username')._unique = False
# CustomUser._meta.get_field('username')._blank = True
# CustomUser._meta.get_field('username')._null = True
