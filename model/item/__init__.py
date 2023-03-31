class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Product(Item):
    def __init__(self, name, price, qtd):
        super().__init__(name, price)
        self.qtd = qtd
    
    def multiPrice(self):
        self.price *= self.qtd

class Service(Item):
     def __init__(self, name, price, description, deadline):
         super().__init__(name, price)
         self.description = description
         self.deadline = deadline