from coffee_shop_challenge.customer import Customer
from coffee_shop_challenge.coffee import Coffee
from coffee_shop_challenge.order import Order

c1 = Customer("Elviss")
c2 = Customer("Tina")

latte = Coffee("Latte")
mocha = Coffee("Mocha")

o1 = Order(c1, latte, 4.5)
o2 = Order(c2, mocha, 5.0)
o3 = Order(c1, latte, 4.0)

print(f"{latte.name} has {latte.num_orders()} orders.")
print(f"Average price for {latte.name}: {latte.average_price()}")

print("Customers who ordered Latte:")
for customer in latte.customers():
    print(customer.name)

print("\norders made by Elviss:") 
for order in c1.orders():
    print(f"{order.coffee.name} :${order.price}")   
