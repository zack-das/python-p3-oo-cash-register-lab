#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0):
        """Initialize with optional discount, total=0, and empty items list"""
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        """Add item with title and price, optional quantity"""
        transaction_total = price * quantity

        self.total += transaction_total
        self.last_transaction_amount = transaction_total

        # Add items to the items list
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        """Apply discount if available, return success/error message"""
        if self.discount == 0:
            print("There is no discount to apply.")
            return False
        else:
            # Calculate discount amount
            discount_amount = self.total * (self.discount / 100)
            # Apply discount to total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
            return True

    def void_last_transaction(self):
        """Remove the last transaction from total and items"""
        # Subtract the last transaction amount from total
        self.total -= self.last_transaction_amount

        if self.total < 0:
            self.total = 0.0
        self.last_transaction_amount = 0
