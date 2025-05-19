import pytest
from order import Order
from customer import Customer
from coffee import Coffee

@pytest.fixture(autouse=True)
def reset_orders():
    Order.all_order.clear
    # Automatically clears all order before each test

def test_valid_order_creation():
    customer = Customer("Elviss")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 4.5)

    assert order.customer == customer  
    assert order.coffee == coffee
    assert order.price == 4.5
    assert order in Order.all_orders  