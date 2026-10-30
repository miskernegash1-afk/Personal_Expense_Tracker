"""
Program Name: Personal Expense Tracker
Author: Misker Negash
Purpose: Saves and loads expense data using JSON.
Starter Code/Resources: Project 1 Personal Expense Tracker.
Date: October 2026
"""

import json
from expense import Expense


def save_expenses(expenses, filename="expenses.json"):
    """Save expenses to a JSON file."""
    data = []
    for expense in expenses:
        data.append(expense.to_dict())

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


  