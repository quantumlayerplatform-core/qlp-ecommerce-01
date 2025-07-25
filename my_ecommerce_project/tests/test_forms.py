from django.test import TestCase
from catalog.forms import ProductForm
from catalog.models import Category

class ProductFormTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Gadgets")

    def test_product_form_valid(self):
        form = ProductForm(data={
            'name': 'New Gadget',
            'category': self.category.id,
            'price': 49.99,
            'stock': 15,
            'description': 'A very useful gadget'
        })
        self.assertTrue(form.is_valid())

    def test_product_form_invalid(self):
        form = ProductForm(data={
            'name': '',
            'category': self.category.id,
            'price': 49.99,
            'stock': 15,
            'description': 'A very useful gadget'
        })
        self.assertFalse(form.is_valid())