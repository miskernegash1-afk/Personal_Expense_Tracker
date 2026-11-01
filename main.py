"""
Program Name: Personal Expense Tracker
Author: Misker Negash
Purpose: This program tracks personal expenses.
Starter Code/Resources: No starter code was used.
Date: November 1, 2026
"""
from tracker import ExpenseTracker
from file_manager import save_expenses, load_expenses
 
"""Display the main program menu."""

def display_menu():
    print("\nPERSONAL EXPENSE TRACKER")
    print("1. Add expense")
    print("2. View expenses")
    print("3. View total")
    print("4. View category total")
    print("5. Exit")

def main():
    tracker = ExpenseTracker()
        
    tracker.expenses = load_expenses()
  # Store one expense and its information together
    while True: 
         display_menu()

         choice = input("Choose 1-5: ")

         if choice == "1":
            name = input("Expense name: ")

            try:
                amount = float(input("Amount: $"))
            except ValueError:
                print("Please enter a valid number.")
                continue

            category = input("Category: ")

            tracker.add_expense(name, amount, category)
            save_expenses(tracker.expenses)

            print("Expense added.")

         elif choice == "2":
            if len(tracker.expenses) == 0:
                print("No expenses yet.")
            else:
                for expense in tracker.expenses:
                    print(
                        expense.name,
                        f"${expense.amount:.2f}",
                        expense.category
                    )

         elif choice == "3":
            print(f"Total spending: ${tracker.get_total():.2f}")

         elif choice == "4":
            category = input("Enter category: ")
            total = tracker.get_category_total(category)

            print(f"{category} spending: ${total:.2f}")

         elif choice == "5":
            save_expenses(tracker.expenses)
            print("Goodbye!")
            break

         else:
            print("Invalid choice.")

    

if __name__ == "__main__":
    main()