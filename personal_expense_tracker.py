"""
Program Name: Personal Expense Tracker
Author: Misker Negash
Purpose: This program tracks personal expenses.
Starter Code/Resources: No starter code was used.
Date: October 2 , 2026
"""
 # Stores all expenses entered by the user
expenses = []

def display_menu():
    print("\nPERSONAL EXPENSE TRACKER")
    print("1. Add expense")
    print("2. View expenses")
    print("3. View total")
    print("4. Exit")
def add_expense():
        
        name = input("Expense name: ")
        amount = float(input("Amount: $"))
        category = input("Category: ")
  # Store one expense and its information together
        expense = {
            "name": name,
            "amount": amount,
            "category": category
        }

        expenses.append(expense)
        print("Expense added.")
    
def view_expenses():

        if len(expenses) == 0:
            print("No expenses yet.")
        else:
            # Display every expense stored in the list
            for expense in expenses:
                print(
                    expense["name"],
                    expense["amount"],
                    expense["category"]
                )
    

def view_total():
        total = 0
     # Add the amount from each expense to the total
        for expense in expenses:
            total = total + expense["amount"]

        print("Total spending: $", total)

def main():
    """Run the Personal Expense Tracker."""
    while True:
        display_menu()

        choice = input("Choose 1-4: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            view_total()

        elif choice == "4":
         print("Goodbye!")
        break
    else:
         print("Invalid choice.")
if __name__ == "__main__":
    main()