from django.test import TestCase


class HomepageTests(TestCase):
    def test_homepage(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)

    def test_coffee_status(self):
        response = self.client.get("/coffee/")
        self.assertEqual(response.status_code, 418)

    def test_coffee_text(self):
        response = self.client.get("/coffee/")
        self.assertEqual(response.content.decode(), "Я чайник")
