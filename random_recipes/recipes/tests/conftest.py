import pytest

from recipes.models import Category


@pytest.fixture
def category(db):
    return Category.objects.create(name='Супы', url_parameter=2)