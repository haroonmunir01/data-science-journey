from book import Book
from member import Member
from library import Library


book_id = 1
member_id = 1

library = Library()


while True:

    print("\n===================================")
    print("       LIBRARY MANAGEMENT SYSTEM")
    print("===================================")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Add Member")
    print("6. View Members")
    print("7. Search Member")
    print("8. Borrow Book")
    print("9. Return Book")
    print("0. Exit")

    choice = input("Enter your choice: ").strip()


    match choice:

        case "1":

            print("\n========== ADD A BOOK ==========")

            title = input("Enter Book Title : ")
            author = input("Enter Book Author Name : ")

            book = Book(title, author, book_id)

            book_id += 1

            library.add_book(book)

            print("Book Has Been Added to the Library")
            
            input("Press Any Key to return to Main Menu...")

        case "2":

            print("\n========== BOOKS ==========")

            library.view_books()

            input("Press Any Key to return to Main Menu...")

        case "3":

            print("\n========== SEARCH BOOK ==========")

            inp = int(input("Enter the Book ID : "))

            library.search_book(inp)

            input("Press Any Key to return to Main Menu...")

        case "4":

            print("\n========== REMOVE BOOK ==========")

            inp = int(input("Enter the Book ID : "))

            library.remove_book(inp)

            input("Press Any Key to return to Main Menu...")


        case "5":

            print("\n========== ADD A MEMBER ==========")

            name = input("Enter Member Name : ")

            member = Member(name, member_id)

            member_id += 1

            library.add_member(member)

            print("Member Has Been Added to the Library")

            input("Press Any Key to return to Main Menu...")

        case "6":

            print("\n========== MEMBERS ==========")

            library.view_members()

            input("Press Any Key to return to Main Menu...")

        case "7":

            print("\n========== SEARCH MEMBER ==========")

            inp = int(input("Enter the Member ID : "))

            library.search_member(inp)

            input("Press Any Key to return to Main Menu...")

        case "8":

            print("\n========== BORROW BOOK ==========")

            member_id_input = int(input("Enter Member ID : "))
            book_id_input = int(input("Enter Book ID : "))

            library.borrow_book(member_id_input, book_id_input)

            input("Press Any Key to return to Main Menu...")


        case "9":

            print("\n========== RETURN BOOK ==========")

            member_id_input = int(input("Enter Member ID : "))
            book_id_input = int(input("Enter Book ID : "))

            library.return_book(member_id_input, book_id_input)

            input("Press Any Key to return to Main Menu...")


        case "0":

            print("Closing the program...")
            break


        case _:

            print("Invalid input. Kindly select a valid option.")