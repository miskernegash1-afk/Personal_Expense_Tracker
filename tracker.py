"""
Program Name: Personal Expense Tracker
Author: Misker Negash
Purpose: Manages expenses and calculates spending totals.
Starter Code/Resources: Project 1 Personal Expense Tracker.
Date: October , 2026
"""

from expense import Expense


class ExpenseTracker:
    """Manage a collection of expenses."""

    def __init__(self):
        """Create an empty expense tracker."""
        self.expenses = []

    def add_expense(self, name, amount, category):
        """Create and add a new expense."""
        expense = Expense(name, amount, category)
        self.expenses.append(expense)

    def get_total(self):
        """Return the total amount of all expenses."""
        total = 0

        for expense in self.expenses:
            total += expense.amount

        return total
    
    def get_category_total(self, category):
        """Return the total spent in one category."""
        total = 0

        for expense in self.expenses:
            if expense.category.lower() == category.lower():
                total += expense.amount

        return total