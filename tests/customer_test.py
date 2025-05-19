import pytest
from customer import Customer
from coffee import Coffee
from order import Order  

class TestCustomer:
    def test_customer_has_name_property(self):
        customer = Customer("Elvis")
        assert customer.name == "Elvis"

    def test_customer_name_setter_validation(self):
        with pytest.raises(Exception):  
            Customer(123)

        with pytest.raises(Exception):
            Customer("")

        with pytest.raises(Exception)
            Customer("A" * 16)

    def test_customer_orders_returns_all_orders_and_coffees(self):
        customer = Customer
        coffee1 = Coffee("Latte") 
        coffee2 = Coffee("Espresso")
        coffee3 = Coffee("Capuccino")
        Order(customer, coffee1, 5.0)                