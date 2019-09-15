import factory
from factory.django import DjangoModelFactory
from posts.models import Post
from users.tests.factories import UserFactory


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.sequence('Title #{}'.format)
    body = factory.sequence('Body #{}'.format)
    author = factory.SubFactory(UserFactory)
