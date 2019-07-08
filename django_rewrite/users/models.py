from django.contrib.auth.models import AbstractUser
from django.db import models
from image_cropping import ImageCropField, ImageRatioField


class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    description = models.CharField(blank=True, max_length=255)

    avatar = ImageCropField(upload_to='avatars/', blank=True)
    cropping = ImageRatioField('avatar', '300x400')
