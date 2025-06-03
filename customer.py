class Customer:
    def __init__(self, name):
        self._validate_name(name)
        self.__name = name
        self.__orders = []

    def _validate_name(self, value):
        if type(value) != str:
            raise TypeError("Customer name must be a string")
        if len(value) < 1 or len(value) > 15:
            raise ValueError("Customer name must be 1 to 15 characters long")

        @property
        
        def name(self):
            return self.__name

        @name.setter
        def name(self, new_name):
            self._validate_name(new_name)
            self.__name = new_name

        def orders(self):
            return self.__orders[:]

        def coffees(self):
            seen = set()
            unique = []
            for order in self.__orders:
                if order.coffee not in seen:
                    seen.add(order.coffee)
                    unique.append(order.coffee)
            return unique
        
        def create_order(self, coffee, price):
            from order import Order
            return Order(self, coffee, price)

        def _log_order(self, order):
            if hasattr(order, "coffee") and hasattr(order, "price"):
                self.__orders.append(order)