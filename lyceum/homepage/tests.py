from django.test import TestCase


class HomepageTests(TestCase):
    def test_homepage(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
