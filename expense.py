"""
Program Name: Personal Expense Tracker
Author: Misker Negash
Purpose: Defines an Expense object.
Starter Code/Resources: Project 1 Personal Expense Tracker.
Date: November 1, 2026
"""


class Expense:
    """Represent one personal expense."""

    def __init__(self, name, amount, category):
        
        self.name = name
        self.amount = amount
        self.category = category
        
    def to_dict(self):
        """Convert the expense into a dictionary for JSON storage."""
        return {
            "name": self.name,
            "amount": self.amount,
            "category": self.category
        }

    @classmethod
    def from_dict(cls, data):
        """Create an Expense object from saved dictionary data."""
        return cls(
            data["name"],
            data["amount"],
            data["category"]
        )