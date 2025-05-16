class Customer:
    def __init__(self, name, email):
        self.name = name

    @property
    def name(self):
        return self._name
    
    # @name.setter
    # def name(self, value):
    #     if not isinstance(value, str):
    #         raise ValueError("Name must be a string")
    #     self._name = value
 


