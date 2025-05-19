import pytest
from coffee import Coffee
from customer import Customer
from order import Order

def test_coffee_initialization_and_name():
    coffee = Coffee("Espresso")
    assert coffee.name == "Espresso"

def    
