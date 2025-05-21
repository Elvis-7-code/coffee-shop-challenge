import pytest
from coffee_shop_challenge.order import Order
from coffee_shop_challenge.customer import Customer
from coffee_shop_challenge.coffee import Coffee
 
# Clear all orders before each test manually (no pytest fixtures for now)
def test_can_create_valid_order():
    Order.all_orders.clear()

    customer = Customer("Elviss")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 4.5)

    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 4.5
    assert order in Order.all_orders  # Make sure it's tracked globally

def test_customer_must_be_customer_instance():
    Order.all_orders.clear()

    coffee = Coffee("Mocha")
    with pytest.raises(TypeError):
        Order("not_a_customer", coffee, 5.0)

def test_coffee_must_be_coffee_instance():
    Order.all_orders.clear()

    customer = Customer("Jane")
    with pytest.raises(TypeError):
        Order(customer, "not_a_coffee", 5.0)

def test_price_must_be_float_and_in_range():
    Order.all_orders.clear()

    customer = Customer("Rick")
    coffee = Coffee("Espresso")

    # Too cheap
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.9)

    # Too expensive
    with pytest.raises(ValueError):
        Order(customer, coffee, 10.5)

    # Not a number
    with pytest.raises(ValueError):
        Order(customer, coffee, "free")

def test_order_is_added_to_global_list():
    Order.all_orders.clear()

    customer = Customer("Tina")
    coffee = Coffee("Flat White")

    Order(customer, coffee, 4.0)
    Order(customer, coffee, 5.0)

    assert len(Order.all_orders) == 2

def test_can_get_orders_for_specific_coffee():
    Order.all_orders.clear()

    customer = Customer("Chris")
    coffee1 = Coffee("Cappuccino")
    coffee2 = Coffee("Americano")

    order1 = Order(customer, coffee1, 3.0)
    order2 = Order(customer, coffee2, 4.0)
    order3 = Order(customer, coffee1, 5.0)

    # Use the class method to get only Cappuccino orders
    cappuccino_orders = Order.orders(coffee1)

    assert cappuccino_orders == [order1, order3]
    assert all(order.coffee == coffee1 for order in cappuccino_orders)
