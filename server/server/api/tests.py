from django.test import TestCase
from rest_framework.test import APIClient

from decimal import Decimal

from .models import Marker

class HelloWorldTestCase(TestCase):
    def test_get_hello_world(self):
        factory = APIClient()

        actual = factory.get('/helloworld/', format='json').data
        expected = {'message': 'Hello World!'}

        self.assertEqual(actual, expected)

class MarkerTestCase(TestCase):
    def test_create_marker(self):
        factory = APIClient()
        request_body = {'latitude': 123.45678, 'longitude': -901.23456, 'altitude': 789.01234}

        actual = factory.post('/markers/', request_body, format='json').data
        expected = [{'id': 1, 'latitude': Decimal('123.45678'), 'longitude': Decimal('-901.23456'), 'altitude': Decimal('789.01234')}]

        self.assertEqual(actual, expected)