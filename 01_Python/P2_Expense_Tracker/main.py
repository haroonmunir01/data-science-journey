import os
import time

expenses=[]
categories = [
    "Food",
    "Transport",
    "Bills",
    "Shopping",
    "Entertainment",
    "Other"
]
def get_amount():
    while True:
        intAmount = input("Enter Amount: ").strip()

        if intAmount == "":
            print("Amount cannot be empty.")
            continue

        try:
            intAmount = float(intAmount)
        except ValueError:
            print("Kindly enter a valid numeric amount.")
            continue

        if intAmount <= 0:
            print("Amount must be greater than 0.")
            continue

        return intAmount
            

def get_description():
    while True:
        description = input("Enter Description: ").strip()

        if description != "":
            return description
        else:
            print("Invalid Input received, Kindly enter a valid description.")

def get_category():
    while True:
        print("Select Category:")

        for i, category in enumerate(categories, 1):
            print(f'{i}) {category}')

        try:
            inp = int(input("Enter Category: "))

            if 1 <= inp <= len(categories):
                return categories[inp - 1]
            else:
                print("Invalid Input received, Kindly enter a valid Category.")
        except ValueError:
            print("Kindly enter a valid number.")

def add_expense():
    intAmount = get_amount()
    intDescription = get_description()
    intCategory = get_category()

    expense = {
        "amount": intAmount,
        "description": intDescription,
        "category": intCategory
    }

    expenses.append(expense)

def view_expenses():
    if len(expenses)<1:
        print("There are no records for expenses ")
    else:    
        for i in expenses:
            print(f'Amount : {i["amount"]}')   
            print(f'Description : {i["description"]}')   
            print(f'Category : {i["category"]}')   
            print("==============")   

def search_expense(des):
    
    for i in expenses:
        if i["description"].lower()==des.lower():
            print(f'Amount : {i["amount"]}')   
            print(f'Description : {i["description"]}')   
            print(f'Category : {i["category"]}') 
            return
                
    print("No record found.")     

def edit_expense(des):
    for i in expenses:
        if i["description"].lower() == des.lower():

            while True:
                print("\n========== Edit Expense ==========")
                print(f'Description: {i["description"]}')
                print(f'Amount: {i["amount"]}')
                print(f'Category: {i["category"]}')
                print("==================================")
                print("1. Edit Description")
                print("2. Edit Amount")
                print("3. Edit Category")
                print("0. Done")

                choice = input("Enter your choice: ")

                match choice:
                    case "1":
                        i["description"] = get_description()
                        print("Description updated successfully.")

                    case "2":
                        i["amount"] = get_amount()
                        print("Amount updated successfully.")

                    case "3":
                        i["category"] = get_category()
                        print("Category updated successfully.")

                    case "0":
                        print("Returning to Main Menu...")
                        return

                    case _:
                        print("Invalid Input. Kindly select a valid option.")

                return

    print("No Expense Found.")        

def delete_expense(des):
    for i in expenses:
        if i["description"].lower() == des.lower():
            expenses.remove(i)
            print("Expense deleted successfully.")
            return

    print("No Expense Found.")

def total_expense():
    count=0
    for i in expenses:
        count+=i["amount"]   
    return count    



while True:
    print("====== Expense Tracker ======")
    print("")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Edit Expense")
    print("5. Delete Expense")
    print("6. Calculate Total")
    print("0. Exit")
    print("")
    choice=input("Enter your choice: ")
    match choice:
        case "1":
            should_exit=False
            while True:
                add_expense()
                print("===================================")
                print("1. Add Another Expense")
                print("2. Back To Menu")
                print("0. Exit")
                inp=input("Enter your choice :")
                exit=0
                if inp=="0":
                    should_exit=True
                    break
                elif inp=="1":
                    continue
                elif inp=="2":
                    break
                else:
                    print("Invalid input , Loading Main Menu.... ")
                    break
            if should_exit:
                break

        case "2":
            view_expenses()
            print("")
            input("Press any key to go back to Main Menu")
            continue

        case "3":
            des=input("Enter the description for the expense you want to search: ")
            search_expense(des)
            print("")
            input("Press any key to go back to Main Menu")
            continue

        case "4":
            des=input("Enter the description for the expense you want to edit: ")
            edit_expense(des)
            print("")
            input("Press any key to go back to Main Menu")
            continue

        case "5":
            des=input("Enter the description for the expense you want to delete: ")
            delete_expense(des)
            print("")
            input("Press any key to go back to Main Menu")
            continue

        case "6":
            total=total_expense()
            print(f"Total Expense: {total}")
            print("")
            input("Press any key to go back to Main Menu")
            continue

        case "0":
            print("Closing the program ...")
            break

        case _:
            print("Invalid Input,Kindly choose correct option from menu ")
        