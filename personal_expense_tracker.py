"""
Program Name: Personal Expense Tracker
Author: Misker Negash
Purpose: This program tracks personal expenses.
Starter Code/Resources: No starter code was used.
Date: September 28, 2026
"""

expenses = []
while True:
    print("\nPERSONAL EXPENSE TRACKER")
    print("1. Add expense")
    print("2. View expenses")
    print("3. View total")
    print("4. Exit")

    choice = input("Choose 1-4: ")
    if choice == "1":
        name = input("Expense name: ")
        amount = float(input("Amount: $"))
        category = input("Category: ")

        expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    print("Expense added.")