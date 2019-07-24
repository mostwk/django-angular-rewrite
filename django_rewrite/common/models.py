from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Rating(models.Model):
    VOTE_UP = 'UP'
    VOTE_DOWN = 'DOWN'

    VOTE_CHOICES = (
        (1, VOTE_UP),
        (-1, VOTE_DOWN),
    )

    user = models.ForeignKey(
        'users.User', related_name='ratings', on_delete=models.CASCADE)
    vote = models.SmallIntegerField(choices=VOTE_CHOICES)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
