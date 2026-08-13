contacts=[]

categories = [
    "Family",
    "Friend",
    "Work",
    "Other"
    ]

def get_name():
    while True:
        inp=input("Enter Contact Name : ").strip()
        if inp=="":
            print("This field can not be empty ")
        elif any(char.isdigit() for char in inp) :
            print("Name can not contain any digit")  
        else:
            return inp   

        
def get_phone():
    while True:
        inp=input("Enter Contact Number : ").strip()
        if inp=="":
            print("This field can not be empty ")
        elif not inp.startswith("0"):
            print("Number must start with a 0")
        elif not inp.isdigit() :
            print("Number must contain only digits")    
        elif len(inp)!=11:
            print("Number must contain exactly 11 Digits")    
        else:
            return inp
        
def get_email():
    while True:
        inp=input("Enter Contact Email : ").strip()
        if inp=="":
            print("This field can not be empty ")
        elif "@" not in inp or ".com" not in inp:
            print("Invalid Email Address ")    
        else:
            return inp    
        
def get_category():

    while True:
        for i,category in enumerate(categories,1):
            print(f'{i}){category}')

        inp=input("Select the Category ").strip()
        try:
            inp=int(inp)
        except ValueError:
            print("Invalid Input")
            continue
        if inp=="":
            print("This field can not be empty ")
        elif inp < 1 or inp > len(categories):
            print("Invalid Input")
        else:
            return categories[inp-1]    



def add_contact():
    inpName=get_name()
    inpPhone=get_phone()
    inpEmail=get_email()
    inpCategory=get_category()

    contact={
            "name": inpName,
            "phone": inpPhone,
            "email": inpEmail,
            "category": inpCategory
            }

    contacts.append(contact)

def view_contact():
    if not contacts:
        print("No contacts found.")
        return

    for i in contacts:
        print(f'Name : {i["name"]}')
        print(f'Phone : {i["phone"]}')
        print(f'Email : {i["email"]}')
        print(f'Category : {i["category"]}')
        print("===================================")

def search_contact(name):
    found = False

    name = name.lower()

    for i in contacts:
        if i["name"].lower() == name:
            print(f'Name : {i["name"]}')
            print(f'Phone : {i["phone"]}')
            print(f'Email : {i["email"]}')
            print(f'Category : {i["category"]}')
            print("===================================")

            found = True
            break

    if not found:
        print("No Contact Found.")

def edit_contact(name):
    found = False
    name = name.lower()

    for i in contacts:
        if i["name"].lower() == name:
            found = True

            print("\n====== Contact Information ======")
            print(f'Name : {i["name"]}')
            print(f'Phone : {i["phone"]}')
            print(f'Email : {i["email"]}')
            print(f'Category : {i["category"]}')
            print("================================")

            while True:
                print("\n====== Edit Contact ======")
                print("1. Edit Name")
                print("2. Edit Phone")
                print("3. Edit Email")
                print("4. Edit Category")
                print("0. Done")

                choice = input("Enter your choice: ")

                match choice:
                    case "1":
                        i["name"] = get_name()
                        print("Name updated successfully.")

                    case "2":
                        i["phone"] = get_phone()
                        print("Phone updated successfully.")

                    case "3":
                        i["email"] = get_email()
                        print("Email updated successfully.")

                    case "4":
                        i["category"] = get_category()
                        print("Category updated successfully.")

                    case "0":
                        break

                    case _:
                        print("Invalid Input.")

            break

    if not found:
        print("No Contact Found.")

def delete_contact(name):
    found = False

    name = name.lower()

    for i in contacts:
        if i["name"].lower() == name:
            contacts.remove(i)
            print("Contact deleted successfully.")
            found = True
            break

    if not found:
        print("No Contact Found.")

while True:
    exit_program = False

    print("====== Contact Book ======")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("0. Exit\n")

    choice = input("Enter your choice: ")

    match choice:

        case "1":
            while True:
                add_contact()

                print("\n===================================")
                print("1. Add Another Contact")
                print("2. Back To Main Menu")
                print("0. Exit")

                inp = input("Enter your choice: ")

                if inp == "1":
                    continue

                elif inp == "2":
                    break

                elif inp == "0":
                    exit_program = True
                    break

                else:
                    print("Invalid Input, Returning to Main Menu...")
                    break

            if exit_program:
                print("Closing the Program...")
                break

            continue

        case "2":
            view_contact()
            input("\nPress any key to return to Main Menu...")
            continue

        case "3":
            name = input("Enter the name of the contact you want to search: ")
            search_contact(name)
            input("\nPress any key to return to Main Menu...")
            continue

        case "4":
            name = input("Enter the name of the contact you want to edit: ")
            edit_contact(name)
            input("\nPress any key to return to Main Menu...")
            continue

        case "5":
            name = input("Enter the name of the contact you want to delete: ")
            delete_contact(name)
            input("\nPress any key to return to Main Menu...")
            continue

        case "0":
            print("Closing the Program...")
            break

        case _:
            print("Invalid Input, Kindly select a valid option.")