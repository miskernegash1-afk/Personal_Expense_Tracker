"""
Program Name: Personal Expense Tracker
Author: Misker Negash
Purpose: Defines an Expense object.
Starter Code/Resources: Project 1 Personal Expense Tracker.
Date: October , 2026
"""


class Expense:
    """Represent one personal expense."""

    def __init__(self, name, amount, category):
        """Create an expense with a name, amount, and category."""
        self.name = name
        self.amount = amount
        self.category = category