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
    
    def coffees(self):
        return list (set(order.coffee for order in self.orders()))
    
    @classmethod
    def most_aficionado(cls, coffee):
        # Customer who spent the most on a specific coffee
        max_spent = 0
        top_customer = None
        for customer in cls.all_customers:
            total_spent = sum(order.price for order in customer.orders()if order.coffee == coffee)
            if total_spent > max_spent:
                max_spent = total_spent
                top_customer = customer
            return top_customer

    

            