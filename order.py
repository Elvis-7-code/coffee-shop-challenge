class Order:
    def __init__(self, customer, coffee, price):
        from customer import Customer
        from coffee import Coffee

        if type(customer) is not Customer:
            raise TypeError("Expected a Customer instance for customer")
        if type(coffee) is not Coffee:
            raise TypeError("Expected a Coffee instance for coffee")

        try:
            price = float(price)
        except ValueError:
            raise TypeError("Price must be a float")

        if price < 1.0 or price > 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")

        self.__customer = customer
        self.__coffee = coffee
        self.__price = price

        @property
        def customer(self):
            return self.__customer

        @property
        def coffee(self):
            return self.__coffee

        @property
        def price(self):
            return self.__price
                 
        if hasattr(customer, "_log_order"):
            customer._log_order(self)

        if hasattr(coffee, "_log_order"):
            coffee._log_order(self)