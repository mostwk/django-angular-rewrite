import factory
import faker
from factory.django import DjangoModelFactory
from users.models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.sequence('User #{}'.format)
    password = faker.Factory.create().password()
