from django.test import TestCase


class CatalogTests(TestCase):
    def test_catalog_page(self):
        response = self.client.get("/catalog/")
        self.assertEqual(response.status_code, 200)

    def test_catalog_item_page(self):
        response = self.client.get("/catalog/1")
        self.assertEqual(response.status_code, 200)

    def test_catalog_item_page_wrong_data(self):
        response = self.client.get("/catalog/test/")
        self.assertEqual(response.status_code, 404)
