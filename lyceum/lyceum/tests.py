__all__ = ["MiddlewareTests"]

from django.test import override_settings, TestCase
from django.urls import reverse

from lyceum import middleware


class MiddlewareTests(TestCase):
    def setUp(self):
        middleware.request_number = 0

    def test_middleware(self):
        for i in range(10):
            response = self.client.get(reverse("homepage:coffee"))
            if i != 9:
                self.assertEqual(response.content.decode(), "Я чайник")
            elif i == 9:
                self.assertEqual(response.content.decode(), "Я кинйач")

    def test_override_false(self):
        with override_settings(ALLOW_REVERSE=False):
            for _ in range(10):
                response = self.client.get(reverse("homepage:coffee"))
                self.assertEqual(response.content.decode(), "Я чайник")
