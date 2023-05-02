"""
    In computer programming, the strategy pattern is a behavioral software design pattern that enables selecting an algorithm at runtime. 
    Instead of implementing a single algorithm directly, code receives run-time instructions as to which in a family of algorithms to use.
    So it allows us to modify an algorithm at runtime.
"""

# *PaymentStrategy


class PaymentStrategy:
    def pay(self, amount):
        pass


#!CreditCardStrategy
class CreditCardStrategy(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} with CreditCard")


#!PayPalStrategy
class PayPalStrategy(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} with PayPal")


#!ShoppingCarts
class ShoppingCart:
    def __init__(self, payment_strategy):
        self.items = []
        self.payment_strategy = payment_strategy

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(item.price for item in self.items)

    def checkout(self):
        total = self.calculate_total()
        self.payment_strategy.pay(total)


#!Item
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# __name__ == _main_
if __name__ == "__main__":
    cc_strategy = CreditCardStrategy()
    paypal_strategy = PayPalStrategy()

    cart = ShoppingCart(cc_strategy)
    cart.add_item(Item("Shirt", 25))
    cart.add_item(Item("Pants", 35))
    cart.checkout()

    cart = ShoppingCart(paypal_strategy)
    cart.add_item(Item("Shoes", 50))
    cart.add_item(Item("Book", 25))
    cart.add_item(Item("Tv", 100))
    cart.checkout()
