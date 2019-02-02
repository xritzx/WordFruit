from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    profile_pic = models.ImageField(upload_to="profile_pic/", blank=True, default="profile.jpg")
