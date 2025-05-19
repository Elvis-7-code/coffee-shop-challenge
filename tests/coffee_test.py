import pytest
from coffee import Coffee
from customer import Customer
from order import Order

def test_coffee_initialization_and_name():
    coffee = Coffee("Espresso")
    assert coffee.name == "Espresso"

def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee(123)

    with pytest.raises(ValueError):
        Coffee("AB") 

def test_coffee_name_is_immutable():
    coffee = Coffee("Cappuccino")
    with pytest.raises(AttributeError):
        coffee.name = "Espresso"

def test_orders_returns_only_this_coffees_orders():
    Order.all_orders.clear()
    c = Customer("Elviss")
    coffee1 = Coffee("Americano")
    coffee2 = Coffee("Mocha")

    Order(c, coffee1, 4.0)
    Order(c, coffee2, 5.0)
    Order(c, coffee1, 6.0)

    assert len(coffee1.orders()) == 2
    assert all(order.coffee == coffee1 for order in coffee1.orders())

def test_customers_returns_unique_customers():
    Order.all_orders.clear()
    c1 = Customer("Elviss")
    c2 = Customer("Zara")
    coffee = Coffee("Flat White")

    Order(c1, coffee, 4.0)
    Order(c2, coffee, 5.0)
    Order(c1, coffee, 6.0)

    customers = coffee.customers()
    assert c1 in customers
    assert c2 in customers
    assert len(customers) == 2  # Unique

def test_num_orders_and_average_price():
    Order.all_orders.clear()
    c = Customer("Eve")
    coffee = Coffee("Cortado")

    assert coffee.num_orders() == 0
    assert coffee.average_price() == 0

    Order(c, coffee, 4.0)
    Order(c, coffee, 6.0)

    assert coffee.num_orders() == 2
    assert coffee.average_price() == 5.0    
