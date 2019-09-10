from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db.models import Model

from .models import Rating

User = get_user_model()


def process_object_rating(*, obj: Model, user: User, vote: str):
    obj_type = ContentType.objects.get_for_model(obj)
    params = {
        'content_type': obj_type,
        'object_id': obj.id,
        'user': user,
    }
    if vote == 0:
        Rating.objects.filter(*params).delete()
    else:
        rating, _ = Rating.objects.update_or_create(
            **params, defaults={'vote': vote})
