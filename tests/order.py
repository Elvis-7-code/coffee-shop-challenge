from coffee import Coffee  # Import the Coffee class from the appropriate module

class Order:
    all_orders = []
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance")
        if not isinstance(price, (float, int)) or not (1.0 <= price <= 10.0):  
            raise ValueError("price must be a number between 1.0 and 10.0")
        
        self.customer = customer
        self.coffee = coffee
        self.price = price

        Order.all_orders.append(self)

        @property
        def price(self):
            return self._price
        
        @property
        def customer(self):
            return self._customer
        
        @property
        def coffee(self):
            return self._coffee
        
        