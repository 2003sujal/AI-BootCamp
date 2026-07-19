class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        self.books.append((title, author))
        print("Book Added!")

    def remove_book(self):
        title = input("Enter Book Title to Remove: ")
        for book in self.books:
            if book[0] == title:
                self.books.remove(book)
                print("Book Removed!")
                return
        print("Book Not Found!")

    def search_book(self):
        key = input("Enter Title or Author: ")
        for book in self.books:
            if key == book[0] or key == book[1]:
                print(book)
                return
        print("Book Not Found!")

    def display_books(self):
        if len(self.books) == 0:
            print("No Books Available")
        else:
            for book in self.books:
                print(book)


lib = Library()

while True:
    print("\n1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Display Books")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        lib.add_book()

    elif choice == "2":
        lib.remove_book()

    elif choice == "3":
        lib.search_book()

    elif choice == "4":
        lib.display_books()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")