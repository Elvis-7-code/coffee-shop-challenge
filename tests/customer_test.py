import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer:
    def test_customer_has_name_property(self):
        customer = Customer("Elvis")
        assert customer.name == "Elvis"