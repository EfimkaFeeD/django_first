from http import HTTPStatus

from django.test import override_settings, TestCase
from django.urls import reverse


class HomepageTests(TestCase):
    def test_homepage(self):
        response = self.client.get(reverse("homepage:home"))
        self.assertEqual(response.status_code, 200)

    def test_coffee_status(self):
        response = self.client.get(reverse("homepage:coffee"))
        self.assertEqual(response.status_code, HTTPStatus.IM_A_TEAPOT)

    def test_coffee_text(self):
        with override_settings(ALLOW_REVERSE=False):
            response = self.client.get(reverse("homepage:coffee"))
            self.assertEqual(response.content.decode(), "Я чайник")
