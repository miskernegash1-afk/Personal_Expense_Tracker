"""
Program Name: Personal Expense Tracker
Author: Misker Negash
Purpose: Tests the ExpenseTracker class.
Starter Code/Resources: Project 1 Personal Expense Tracker.
Date: October 20, 2026
"""

from tracker import ExpenseTracker


def test_add_expense():
    """Test that an expense can be added."""
    tracker = ExpenseTracker()

    tracker.add_expense("Gas", 40.00, "Transportation")

    assert len(tracker.expenses) == 1
    assert tracker.expenses[0].name == "Gas"


def test_total():
    """Test that the total expense calculation is correct."""
    tracker = ExpenseTracker()

    tracker.add_expense("Gas", 40.00, "Transportation")
    tracker.add_expense("Food", 20.00, "Food")

    assert tracker.get_total() == 60.00
