from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from image_cropping import ImageCropField, ImageRatioField


class User(AbstractUser):
    username = models.CharField(
        _('username'),
        max_length=15,
        unique=True,
        error_messages={
            'unique': _("A user with that username already exists."),
        },
        validators=[MinLengthValidator(4)]
    )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    description = models.CharField(blank=True, max_length=255)

    avatar = ImageCropField(upload_to='avatars/', blank=True)
    cropping = ImageRatioField('avatar', '300x400')

    def __str__(self):
        return self.user.username
