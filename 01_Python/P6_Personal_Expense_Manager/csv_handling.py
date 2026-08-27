
import csv
import os

def create_file():
    if not os.path.exists("expenses.csv") or os.path.getsize("expenses.csv") == 0:
        with open("expenses.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "amount", "category", "description"])
            
def get_next_id():
    try:
        with open("expenses.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)

            ids = [int(row[0]) for row in reader if row]

            if ids:
                return max(ids) + 1

            return 1

    except FileNotFoundError:
        return 1
    
def save_expense(id,amount,cat,description):
    with open("expenses.csv","a",newline="") as file:
        write=csv.writer(file)
        write.writerow([id,amount,cat,description])

def get_expenses():
    with open("expenses.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)        

def save_expenses(expenses):
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["id", "amount", "category", "description"])

        for expense in expenses:
            writer.writerow([
                expense["id"],
                expense["amount"],
                expense["category"],
                expense["description"]
            ])    
