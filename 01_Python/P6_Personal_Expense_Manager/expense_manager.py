import csv_handling

categories = [
    "Food",
    "Transport",
    "Shopping",
    "Bills",
    "Entertainment",
    "Health",
    "Education",
    "Rent",
    "Utilities",
    "Travel",
    "Subscriptions",
    "Other"
]


def add_expense():
    id=csv_handling.get_next_id()
    while True:
        amount=input("Enter the Amount : ").strip()
        if amount=="":
            print("Amount can not be empty")
            continue
        try:
            amount=float(amount)    
            break
        except ValueError:
            print("Amount must be a number ")
            continue

    while True:
        print("Categories : ")
        for i,cat in enumerate(categories,1):
            print(f"{i}) {cat}")

        category=input("Choose Expense Category : ")
        if category=="":
            print("Category field can not be empty")
            continue
        try:
            category=int(category)    

        except ValueError:
            print("Choose the valid number from menu ")
            continue

        if category<1 or category > len(categories):
            print("Choose the valid number from menu ")
            continue
        else:
            finalCategory=categories[category-1]
            break

    while True:
        description=input('Enter Description for the expense : ').strip()
        if description=="":
            print("Description field can not be empty")    
            continue  
        else:
            break              

    csv_handling.save_expense(id,amount,finalCategory,description)      
    print("Expenses Added Successfully ")  



def view_expenses():
    expenses = csv_handling.get_expenses()

    if not expenses:
        print("No expenses found.")
        return

    print("\n========== EXPENSES ==========")

    for expense in expenses:
        print(f"ID          : {expense['id']}")
        print(f"Amount      : {expense['amount']}")
        print(f"Category    : {expense['category']}")
        print(f"Description : {expense['description']}")
        print("------------------------------")

def search_expense():
    expenses = csv_handling.get_expenses()

    if not expenses:
        print("No expenses found.")
        return

    expense_id = input("Enter Expense ID: ").strip()

    for expense in expenses:
        if expense["id"] == expense_id:
            print("\n========== EXPENSE ==========")
            print(f"ID          : {expense['id']}")
            print(f"Amount      : {expense['amount']}")
            print(f"Category    : {expense['category']}")
            print(f"Description : {expense['description']}")
            return

    print("Expense not found.")

def delete_expense():
    expenses = csv_handling.get_expenses()

    if not expenses:
        print("No expenses found.")
        return

    expense_id = input("Enter Expense ID: ").strip()

    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            csv_handling.save_expenses(expenses)
            print("Expense has been deleted.")
            return

    print("Expense not found.")
