from django.test import TestCase, Client
from django.urls import reverse
from catalog.models import Product, Category

class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="Books")
        self.product = Product.objects.create(
            name="Django for Beginners",
            category=self.category,
            price=39.99,
            stock=50,
            description="Learn Django effectively"
        )
        self.list_url = reverse('catalog:product_list')
        self.detail_url = reverse('catalog:product_detail', args=[self.product.id])

    def test_product_list_view(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Django for Beginners")

    def test_product_detail_view(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Learn Django effectively")
        self.assertContains(response, "39.99")