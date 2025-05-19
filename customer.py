class Customer:
    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not (1 <= len(value) <= 50):
            raise ValueError("Name must be between 1 and 50 characters long")
        self._name = value