from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

from .models import Rating

User = get_user_model()


def process_object_rating(*, obj, user: User, vote: str) -> Rating:
    obj_type = ContentType.objects.get_for_model(obj)
    params = {
        'content_type': obj_type,
        'object_id': obj.id,
        'user': user,
    }
    if vote == 0:
        Rating.objects.filter(*params).delete()
    else:
        # params.update({'vote': vote})
        rating, _ = Rating.objects.update_or_create(
            **params, defaults={'vote': vote})
