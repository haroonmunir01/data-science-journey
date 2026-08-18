import random 
question = {

    "What is the purpose of a loop?": [
        "Store data",
        "Repeat a block of instructions",
        "Define a function",
        "Stop a program"
    ],

    "What is a variable?": [
        "A named storage location for data",
        "A type of loop",
        "A programming error",
        "A comment"
    ],

    "What is the purpose of a function?": [
        "To repeat the entire program",
        "To store only numbers",
        "To create a reusable block of code",
        "To delete variables"
    ],

    "What does an if statement allow a program to do?": [
        "Repeat code automatically",
        "Make decisions based on conditions",
        "Store multiple values",
        "Create a computer"
    ],

    "What is a data type?": [
        "A programming language",
        "A type of computer",
        "A classification of the kind of data",
        "A type of loop"
    ],

    "What is the purpose of a return statement in a function?": [
        "To stop the computer",
        "To send a value back from the function",
        "To create a variable",
        "To start a loop"
    ],

    "What is an array or list commonly used for?": [
        "Storing multiple values",
        "Running the operating system",
        "Creating errors",
        "Defining conditions only"
    ],

    "What is an argument in a function call?": [
        "An error in the function",
        "A value passed to the function",
        "The function's name",
        "A loop inside the function"
    ],

    "What does the == operator generally do?": [
        "Assign a value",
        "Add two values",
        "Compare two values for equality",
        "End a program"
    ],

    "What is an infinite loop?": [
        "A loop that runs exactly once",
        "A loop that never executes",
        "A loop that continues without reaching its stopping condition",
        "A loop that always produces an error"
    ]
}


answer = {

    "What is the purpose of a loop?":
        "Repeat a block of instructions",

    "What is a variable?":
        "A named storage location for data",

    "What is the purpose of a function?":
        "To create a reusable block of code",

    "What does an if statement allow a program to do?":
        "Make decisions based on conditions",

    "What is a data type?":
        "A classification of the kind of data",

    "What is the purpose of a return statement in a function?":
        "To send a value back from the function",

    "What is an array or list commonly used for?":
        "Storing multiple values",

    "What is an argument in a function call?":
        "A value passed to the function",

    "What does the == operator generally do?":
        "Compare two values for equality",

    "What is an infinite loop?":
        "A loop that continues without reaching its stopping condition"
}


def start_quiz():
    question_list = list(question.keys())
    score=0
    random.shuffle(question_list)
    print("====== Programming Quiz ======")
    
    for i,val in enumerate(question_list,1):
        print(f"Question : {i}")
        print(val)
        print("")
        count=len(question[val])
        for  index,value in enumerate(question[val],1):
            print (f"{index}. {value}")
            
        while True:
            inp=input("Enter Your Choice : ").strip()
            if inp=="":
                print("This field can not be empty")
                continue
            try:
                inp=int(inp)
            except ValueError:
                print("Invalid Input ,Kindly choose a digit from menu")
                continue
            if inp<=0 or inp>count:
                print("Kindly choose a digit from menu")
                continue
            else :
                break                
        if answer[val]==question[val][inp-1]:
            score=score+1
        print("")    

    print(f"Your Total Score is {score}/10")   

def show_instructions():
    print("\n====== Quiz Instructions ======")
    print("1. The quiz contains 10 programming concept questions.")
    print("2. Each question has 4 options.")
    print("3. Enter the number corresponding to your answer.")
    print("4. Only one answer is correct for each question.")
    print("5. Questions will appear in a random order.")
    print("6. Your score will be displayed at the end of the quiz.")
    print("7. You must enter a valid option before moving to the next question.")
               

while True:
    print("\n===================================")
    print("       PROGRAMMING CONCEPT QUIZ")
    print("===================================")
    print("1. Start Quiz")
    print("2. View Instructions")
    print("0. Exit")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            start_quiz()
            break
        
        case "2":
            show_instructions()
            input("\nPress any key to return to Main Menu...")
            continue
        
        case "0":
            print("Closing the Program...")
            break
        
        case _:
            print("Invalid Input. Kindly select a valid option.")