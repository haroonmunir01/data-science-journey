class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def view_books(self):
        for book in self.books:
            print(f" Book Title : {book.title}")
            print(f" Book Author : {book.author}")
            print(f" Book ID : {book.book_id}")
            print(f" Book Availability : {book.available}")
            print("")

    def search_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                print(f" Book Title : {book.title}")
                print(f" Book Author : {book.author}")
                print(f" Book ID : {book.book_id}")
                print(f" Book Availability : {book.available}")
                print("")
                return

        print("Book Not Found")

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:

                if not book.available:
                    print("Book is currently borrowed.")
                    return

                self.books.remove(book)
                print("Book has been Removed From Library")
                print("")
                return

        print("Book Not Found")

    def add_member(self, member):
        self.members.append(member)

    def view_members(self):
        for member in self.members:
            print(f" Member Name : {member.name}")
            print(f" Member ID : {member.member_id}")

            if member.borrowed_books:
                print(" Borrowed Books :")

                for book in member.borrowed_books:
                    print(f"   - {book.title} (ID: {book.book_id})")
            else:
                print(" Borrowed Books : None")

            print("")

    def search_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:

                print(f" Member Name : {member.name}")
                print(f" Member ID : {member.member_id}")

                if member.borrowed_books:
                    print(" Borrowed Books :")

                    for book in member.borrowed_books:
                        print(f"   - {book.title} (ID: {book.book_id})")
                else:
                    print(" Borrowed Books : None")

                print("")
                return

        print("Member Not Found")

    def borrow_book(self, member_id, book_id):

        member_found = False
        book_found = False

        for member in self.members:
            if member.member_id == member_id:
                member_found = True
                break

        for book in self.books:
            if book.book_id == book_id:
                book_found = True
                break

        if not member_found:
            print("Member Not Found")
            return

        if not book_found:
            print("Book Not Found")
            return

        if not book.available:
            print("Book is already borrowed")
            return

        for borrowed_book in member.borrowed_books:
            if borrowed_book.book_id == book_id:
                print("This member already has this book")
                return

        member.borrowed_books.append(book)
        book.available = False

        print("Book has been borrowed successfully")

    def return_book(self, member_id, book_id):

        member_found = False
        book_found = False

        for member in self.members:
            if member.member_id == member_id:
                member_found = True
                break

        for book in self.books:
            if book.book_id == book_id:
                book_found = True
                break

        if not member_found:
            print("Member Not Found")
            return

        if not book_found:
            print("Book Not Found")
            return

        for borrowed_book in member.borrowed_books:
            if borrowed_book.book_id == book_id:

                member.borrowed_books.remove(borrowed_book)
                book.available = True

                print("Book has been returned successfully")
                return

        print("This member has not borrowed this book")