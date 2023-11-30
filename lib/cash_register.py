#!/usr/bin/env python3

class CashRegister:
    def __init__(self):
        self.items = []  # List to keep track of items
        self.prices = []  # List to keep track of item prices
        self.quantities = []  # List to keep track of item quantities

    def add_item(self, item, price, quantity=1):
        self.items.append(item)
        self.prices.append(price)
        self.quantities.append(quantity)

    def calculate_total(self):
        total = sum(price * quantity for price, quantity in zip(self.prices, self.quantities))
        return total

    def apply_discount(self, discount_percentage=""):
        discount_factor = 1 - discount_percentage / 100
        self.prices = [price * discount_factor for price in self.prices]

    def void_last_transaction(self):
        if not self.items:
            print("No transactions to void.")
            return

        self.items.pop()
        self.prices.pop()
        self.quantities.pop()

    def display_receipt(self):
        for item, price, quantity in zip(self.items, self.prices, self.quantities):
            print(f"{item} x{quantity}: ${price:.2f} each")
     