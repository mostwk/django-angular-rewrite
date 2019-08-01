import pytest
from posts.tests.factories import PostFactory

from django_rewrite.authentication.tests.apis.conftest import *  # noqa


@pytest.fixture
def populate_posts():
    PostFactory.generate_batch('create', 5)
