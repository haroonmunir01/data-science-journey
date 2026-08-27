import csv_handling
import expense_manager

csv_handling.create_file()

while True:
    print("\n===================================")
    print("       PERSONAL EXPENSE MANAGER")
    print("===================================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Delete Expense")
    print("0. Exit")

    choice = input("Enter your choice: ").strip()

    match choice:
        case "1":
            expense_manager.add_expense()
            input(" Press any key to return to Menu ")
            continue

        case "2":
            expense_manager.view_expenses()
            input(" Press any key to return to Menu ")
            continue

        case "3":
            expense_manager.search_expense()
            input(" Press any key to return to Menu ")
            continue            

        case "4":
            expense_manager.delete_expense()
            input(" Press any key to return to Menu ")
            continue             

        case "0":
            print("Closing the program...")
            break

        case _:
            print("Invalid input.")