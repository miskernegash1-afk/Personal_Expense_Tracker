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
        data.append({
            "name": expense.name,
            "amount": expense.amount,
            "category": expense.category
        })

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load_expenses(filename="expenses.json"):
    """Load expenses from a JSON file."""
    try:
        with open(filename, "r") as file:
            data = json.load(file)

        expenses = []

        for item in data:
            expense = Expense(
                item["name"],
                item["amount"],
                item["category"]
            )
            expenses.append(expense)

        return expenses

    except FileNotFoundError:
        return []