from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Elviss")
c2 = Customer("Tina")

latte = Coffee("Latte")
mocha = Coffee("Mocha")

o1 = Order(c1, latte, 4.5)
o2 = Order(c2, mocha, 5.0)
o3 = Order(c1, latte, 4.0)

print(f"{latte.name} has {latte.num_orders()} orders.")
print(f"Average price for {latte.name}: {latte.average_price()}")