from django.db import models

from common.mixins import TrackableDateModelMixin, RatedModelMixin


class Post(TrackableDateModelMixin, RatedModelMixin, models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    body = models.TextField(max_length=500)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.title
