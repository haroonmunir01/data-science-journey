import time
import os


students=[]
def addStudent():
    nameInp=input("Enter Student Name : ")
    ageInp=int(input("Enter Student Age : "))
    courseInp=input("Enter Student Course: ")

    std={"name":nameInp,"age":ageInp,"course":courseInp}
    students.append(std)
    print("Student Added Successfully.")

def viewStudents():
    for i in students:
        print(f'Student Name: {i["name"]}')
        print(f'Student Age: {i["age"]}')
        print(f'Student Course: {i["course"]}')
        print("===================================")

def searchStudent(name):
    found = False
    for i in students:
        if name==i["name"]:
            print(f'Student Name: {i["name"]}')
            print(f'Student Age: {i["age"]}')
            print(f'Student Course: {i["course"]}')
            found=True
            break
            
    if not found:   
        print("No Student Record Found")
        

while True:
    print("====== Student Record Manager ======")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("0. Exit\n")

    choice =input("Enter your choice : ")
    match choice:

        case "1":
            while(choice=="1"):
                addStudent()
                print("1. Add Another Student")
                print("2. Back to Main Menu")
                print("0. Exit")
                choice=input("Enter your choice : ")
                if choice=="1":
                    continue
                elif choice=="2":
                    break
                elif choice=="0":
                    print("Closing Program")
                else :
                    print("Invalid Input , CLosing Program")
            if choice=="2":        
                continue    
            else :
                break           

        case "2":
            viewStudents()
            input("Press any key to continue")
            print("Returning to Menu.....")
            time.sleep(3)
            os.system("cls")
            continue
                
        case "3":
            name=input("Enter the name of the student you want to search : ")
            searchStudent(name)
            input("Press any key to continue")
            print("Returning to Menu.....")
            time.sleep(3)
            os.system("cls")
            continue

        case "0":
            break
        
        case _:
            print("Invalid Input , Kindly select valid option from Menu")



