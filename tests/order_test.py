import pytest
from order import Order
from customer import Customer
from coffee import Coffee

@pytest.fixture(autouse=True)
def reset_orders():
    Order.all_order.clear
    # Automatically clears all order before each test