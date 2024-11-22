import pytest
from django.conf import settings
from django.test.client import Client
from django.urls import reverse

def test_get_recipe(category):
    assert 