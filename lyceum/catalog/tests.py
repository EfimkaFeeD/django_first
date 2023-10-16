from django.test import TestCase


class CatalogTests(TestCase):
    def test_catalog_page(self):
        response = self.client.get("/catalog/")
        self.assertEqual(response.status_code, 200)

    def test_catalog_item_page(self):
        response = self.client.get("/catalog/1/")
        self.assertEqual(response.status_code, 200)

    def test_catalog_item_page_wrong_data(self):
        response = self.client.get("/catalog/test/")
        self.assertEqual(response.status_code, 404)

    def test_catalog_re_item_page(self):
        response = self.client.get("/catalog/re/2/")
        self.assertContains(response, status_code=200, text=2)

    def test_catalog_re_item_page_wrong_data(self):
        response = self.client.get("/catalog/re/test2/")
        self.assertEqual(response.status_code, 404)

    def test_catalog_conv_item_page(self):
        response = self.client.get("/catalog/converter/3/")
        self.assertContains(response, status_code=200, text=3)

    def test_catalog_conv_item_page_wrong_data(self):
        response = self.client.get("/catalog/converter/test3/")
        self.assertEqual(response.status_code, 404)
