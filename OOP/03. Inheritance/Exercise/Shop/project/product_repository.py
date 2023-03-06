from project.product import Product


class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        product = next(filter(lambda p: p.name == product_name, self.products), None)
        if product is not None:
            return product

    def remove(self, product_name):
        [self.products.remove(p) for p in self.products if p.name == product_name]

    def __repr__(self):
        return "\n".join(f"{obj.name}: {obj.quantity}" for obj in self.products)
