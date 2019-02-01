from django.db import models
from django.contrib.auth.models import AbstractUser
from stdimage import StdImageField

class CustomUser(AbstractUser):

    profile_pic = models.ImageField(upload_to="profile_pic/", blank=True, default="profile.jpg")
