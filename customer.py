from order import Order
class Customer:
    def __init__(self, name):
        self.name = name
        Customer.all_customers.append(self)
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters long")
        self._name = value

    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    def orders(self):
        return [order for order in Order.all_orders if order.customer == self]
    

    

            