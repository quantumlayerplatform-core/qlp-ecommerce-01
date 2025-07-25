from django.test import TestCase
from catalog.models import Product, Category
from django.core.exceptions import ValidationError

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Electronics")
        
    def test_product_creation(self):
        product = Product.objects.create(
            name="Laptop",
            category=self.category,
            price=999.99,
            stock=10,
            description="High performance laptop"
        )
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.category.name, "Electronics")
        self.assertEqual(product.price, 999.99)
        self.assertEqual(product.stock, 10)
        self.assertEqual(product.description, "High performance laptop")

    def test_product_str(self):
        product = Product.objects.create(
            name="Smartphone",
            category=self.category,
            price=299.99,
            stock=20,
            description="Latest model smartphone"
        )
        self.assertEqual(str(product), "Smartphone")

    def test_negative_price(self):
        with self.assertRaises(ValidationError):
            Product.objects.create(
                name="Tablet",
                category=self.category,
                price=-50,
                stock=5,
                description="Tablet with negative price"
            ).full_clean()