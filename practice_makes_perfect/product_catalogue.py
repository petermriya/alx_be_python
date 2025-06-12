class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_value(self):
        return self.quantity * self.price

    def product_info(self):
        print (f"Product name: {self.name}")
        print (f"Product price: {self.price}")
        print (f"Product quantity: {self.quantity}")
        print (f"Product value: {self.total_value()}")

product1 = Product ("Laptops", 30000, 100)

product1.product_info()
