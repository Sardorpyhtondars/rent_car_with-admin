class Product:
    def __init__(self, name, title, price, quantity):
        self.name = name
        self.title = title
        self.price = price
        self.quantity = quantity


class Order:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def basket(self):
        order = Order(self.product, self.quantity)
        price = self.product.price
        quantity = self.quantity
        total = price * quantity
        return order, total


class Settings:
    def __init__(self):
        kod = input(
            "What do you want to do?\n 1. Change product name\n 2. Change product title\n 3. Change product price\n 4. Change product quantity\n")
