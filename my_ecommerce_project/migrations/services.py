from .models import Product

class ProductService:
    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_product_by_id(product_id):
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return None

    @staticmethod
    def create_product(name, description, price, stock):
        product = Product(name=name, description=description, price=price, stock=stock)
        product.save()
        return product

    @staticmethod
    def update_product(product_id, name, description, price, stock):
        product = ProductService.get_product_by_id(product_id)
        if product:
            product.name = name
            product.description = description
            product.price = price
            product.stock = stock
            product.save()
            return product
        return None

    @staticmethod
    def delete_product(product_id):
        product = ProductService.get_product_by_id(product_id)
        if product:
            product.delete()
            return True
        return False