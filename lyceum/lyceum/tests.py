from django.test import TestCase, override_settings

from . import middleware


class MiddlewareTests(TestCase):
    def setUp(self):
        middleware.request_number = 0

    def test_middleware(self):
        with override_settings(ALLOW_REVERSE=True):
            for i in range(10):
                response = self.client.get("/coffee/")
                if i != 9:
                    self.assertEqual(response.content.decode(), "Я чайник")
                elif i == 9:
                    self.assertEqual(response.content.decode(), "Я кинйач")

    def test_false(self):
        for _ in range(10):
            response = self.client.get("/coffee/")
            self.assertEqual(response.content.decode(), "Я чайник")
