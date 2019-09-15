from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models import Sum
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Rating
from .services import process_object_rating


class TrackableDateModelMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class RatedModelMixin(models.Model):
    rating = GenericRelation(Rating)

    class Meta:
        abstract = True

    @property
    def votes(self):
        return self.rating.aggregate(Sum('vote'))['vote__sum'] or 0


class RatedApiMixin:

    @action(
        methods=['POST'],
        detail=True,
        url_path='vote/(?P<vote>-1|0|1?)',
        permission_classes=(IsAuthenticated, ),
    )
    def vote(self, request, vote, pk=None, **kwargs):
        obj = self.get_object()
        process_object_rating(obj=obj, user=request.user, vote=vote)
        return Response({'ok': True, 'votes': obj.votes})
