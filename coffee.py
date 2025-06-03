class Coffee:
    def __init__(self, name):
        name = name.strip()
        if not isinstance(name, str):
            raise TypeError("Expected name to be a string")
        if len(name) < 3:
            raise ValueError("Name must have at least 3 characters")
        
        self.__orders = []
        self.__name = name

    @property
    def name(self):
        return self.__name

    def orders(self):
        return list(self.__orders)

    def num_orders(self):
        return len(self.__orders)

    def average_price(self):
        count = self.num_orders()
        if count == 0:
            return 0
        total = 0
        for order in self.__orders:
            total += order.price
            return total / count
    
        def customers(self):
            collected = []
            identifiers = set()
            for o in self.__orders:
                cust = o.customer
                if cust not in identifiers:
                    collected.append(cust)
                    identifiers.add(cust)
            return collected

    def _log_order(self, order):
        if hasattr(order, "price") and hasattr(order, "customer"):
            self.__orders.append(order)