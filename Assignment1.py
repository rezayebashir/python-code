from abc import ABC, abstractmethod
from datetime import date, timedelta



class Person(ABC):
    """Abstract base class representing a person."""

    def __init__(self, person_id, name, email):
        self.__person_id = person_id
        self.name = name
        self.email = email

    @property
    def person_id(self):
        return self.__person_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string.")
        self.__name = value.strip()

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if not isinstance(value, str) or "@" not in value:
            raise ValueError("Invalid email address.")
        self.__email = value.strip()

    @abstractmethod
    def get_role(self):
        """Return the role of the person."""
        pass

    def __str__(self):
        return f"{self.name} ({self.get_role()})"



class Member(Person):
    """Library member who can borrow books."""

    def __init__(self, person_id, name, email, membership_type="Regular"):
        super().__init__(person_id, name, email)
        self.membership_type = membership_type
        self.__active_loans = []

    @property
    def membership_type(self):
        return self.__membership_type

    @membership_type.setter
    def membership_type(self, value):
        allowed = ["Regular", "Premium", "Student"]

        if value not in allowed:
            raise ValueError(
                f"Membership type must be one of: {allowed}"
            )

        self.__membership_type = value

    @property
    def active_loans(self):
        # Return a copy to protect internal data
        return self.__active_loans.copy()

    def add_loan(self, loan):
        if loan not in self.__active_loans:
            self.__active_loans.append(loan)

    def remove_loan(self, loan):
        if loan in self.__active_loans:
            self.__active_loans.remove(loan)

    def get_role(self):
        return "Member"

    # Method overriding
    def __str__(self):
        return (
            f"Member: {self.name} | "
            f"ID: {self.person_id} | "
            f"Type: {self.membership_type}"
        )


class Librarian(Person):
    """Library employee responsible for managing books and loans."""

    def __init__(self, person_id, name, email, employee_id):
        super().__init__(person_id, name, email)
        self.employee_id = employee_id

    def get_role(self):
        return "Librarian"

    def issue_loan(self, member, book):
        return Loan(member, book)

    def __str__(self):
        return (
            f"Librarian: {self.name} | "
            f"Employee ID: {self.employee_id}"
        )


class Book:
    """Represents a book in the library."""

    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.__available = True

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, value):
        if not isinstance(value, str) or len(value.strip()) < 5:
            raise ValueError("ISBN must be a valid string.")
        self.__isbn = value.strip()

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Title cannot be empty.")
        self.__title = value.strip()

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Author cannot be empty.")
        self.__author = value.strip()

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Year must be a positive integer.")
        self.__year = value

    @property
    def available(self):
        return self.__available

    def borrow(self):
        if not self.__available:
            raise ValueError("Book is already borrowed.")

        self.__available = False

    def return_book(self):
        self.__available = True

    def __str__(self):
        status = "Available" if self.available else "Borrowed"

        return (
            f"{self.title} by {self.author} "
            f"({self.year}) - {status}"
        )




class Loan:
    """Represents a book loan made by a member."""

    loan_counter = 1

    def __init__(self, member, book, days=14):
        if not isinstance(member, Member):
            raise TypeError("Loan must belong to a Member.")

        if not isinstance(book, Book):
            raise TypeError("Loan must contain a Book.")

        if days <= 0:
            raise ValueError("Loan duration must be positive.")

        if not book.available:
            raise ValueError("Book is already borrowed.")

        self.loan_id = Loan.loan_counter
        Loan.loan_counter += 1

        self.member = member
        self.book = book
        self.borrow_date = date.today()
        self.due_date = self.borrow_date + timedelta(days=days)
        self.returned = False

        # Mark book as borrowed
        book.borrow()

        # Add loan to member
        member.add_loan(self)

    def return_book(self):
        if self.returned:
            raise ValueError("Book has already been returned.")

        self.book.return_book()
        self.member.remove_loan(self)
        self.returned = True

    def __str__(self):
        status = "Returned" if self.returned else "Active"

        return (
            f"Loan #{self.loan_id}: "
            f"{self.book.title} -> {self.member.name} | "
            f"Due: {self.due_date} | {status}"
        )




class Library:
    """Main library class managing books, members and loans."""

    def __init__(self, name):
        self.name = name

        # Composition
        self.__books = []
        self.__members = []
        self.__loans = []

    # ---------------- BOOK MANAGEMENT ----------------

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only Book objects can be added.")

        if self.find_book(book.isbn):
            raise ValueError("A book with this ISBN already exists.")

        self.__books.append(book)

    def find_book(self, isbn):
        for book in self.__books:
            if book.isbn == isbn:
                return book
        return None

    # ---------------- MEMBER MANAGEMENT ----------------

    def add_member(self, member):
        if not isinstance(member, Member):
            raise TypeError("Only Member objects can be added.")

        if self.find_member(member.person_id):
            raise ValueError("Member already exists.")

        self.__members.append(member)

    def find_member(self, member_id):
        for member in self.__members:
            if member.person_id == member_id:
                return member
        return None

    # ---------------- LOAN MANAGEMENT ----------------

    def borrow_book(self, member_id, isbn, days=14):
        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if member is None:
            raise ValueError("Member not found.")

        if book is None:
            raise ValueError("Book not found.")

        loan = Loan(member, book, days)
        self.__loans.append(loan)

        return loan

    def return_book(self, loan_id):
        for loan in self.__loans:
            if loan.loan_id == loan_id:
                loan.return_book()
                return

        raise ValueError("Loan not found.")

    # ---------------- DISPLAY METHODS ----------------

    def list_books(self):
        print("\n--- BOOKS ---")

        if not self.__books:
            print("No books available.")
            return

        for book in self.__books:
            print(book)

    def list_members(self):
        print("\n--- MEMBERS ---")

        if not self.__members:
            print("No members registered.")
            return

        for member in self.__members:
            print(member)

    def list_loans(self):
        print("\n--- LOANS ---")

        if not self.__loans:
            print("No loans available.")
            return

        for loan in self.__loans:
            print(loan)

    def __str__(self):
        return (
            f"Library: {self.name} | "
            f"Books: {len(self.__books)} | "
            f"Members: {len(self.__members)} | "
            f"Loans: {len(self.__loans)}"
        )




def main():

    # Create Library
    library = Library("Central City Library")

    # Create Books
    book1 = Book(
        "ISBN001",
        "Python Programming",
        "John Smith",
        2024
    )

    book2 = Book(
        "ISBN002",
        "Object Oriented Programming",
        "Jane Brown",
        2023
    )

    book3 = Book(
        "ISBN003",
        "Clean Code",
        "Robert Martin",
        2008
    )

    # Add books to library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Create Members
    member1 = Member(
        "M001",
        "Ali Ahmad",
        "ali@example.com",
        "Student"
    )

    member2 = Member(
        "M002",
        "Sara Khan",
        "sara@example.com",
        "Premium"
    )

    # Add members
    library.add_member(member1)
    library.add_member(member2)

    # Create Librarian
    librarian = Librarian(
        "L001",
        "David Wilson",
        "david@library.com",
        "EMP100"
    )


    print("\n=== POLYMORPHISM ===")

    people = [member1, member2, librarian]

    for person in people:
        print(person)
        print("Role:", person.get_role())


    print("\n=== LIBRARY ===")
    print(library)

    library.list_books()
    library.list_members()

   

    print("\n=== BORROWING BOOK ===")

    loan1 = library.borrow_book(
        "M001",
        "ISBN001",
        14
    )

    print("New loan created:")
    print(loan1)


    loan2 = library.borrow_book(
        "M002",
        "ISBN002",
        7
    )

    print("\nSecond loan:")
    print(loan2)

    

    library.list_loans()

   

    print("\n=== RETURN BOOK ===")

    library.return_book(loan1.loan_id)

    print("Book returned successfully.")

    library.list_books()
    library.list_loans()

   

    print("\n=== ENCAPSULATION / VALIDATION ===")

    try:
        member1.email = "invalid-email"
    except ValueError as error:
        print("Validation error:", error)

    try:
        book1.title = ""
    except ValueError as error:
        print("Validation error:", error)




if __name__ == "__main__":
    main()
