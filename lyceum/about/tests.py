__all__ = ["AboutTests"]

from django.test import TestCase
from django.urls import reverse


class AboutTests(TestCase):
    def test_about_page(self):
        response = self.client.get(reverse("about:description"))
        self.assertEqual(response.status_code, 200)
