class Library:
    def __init__(self, file_name="books.txt"):
        self.file_name = file_name
        self.file = open(self.file_name, "a+")  


    def __del__(self):
        if hasattr(self, 'file') and self.file:
            self.file.close()  


    def list_books(self):
        self.file.seek(0)  
        books = self.file.read().splitlines()
        if not books:
            print("No books available.")
        else:
            for book in books:
                book_info = book.split(',')
                print(f"Book: {book_info[0]}, Author: {book_info[1]}, Release Date: {book_info[2]}, Pages: {book_info[3]}")


    def add_book(self):
        book_title = input("Enter book title: ")
        author = input("Enter author name: ")
    
        while True:
            release_year = input("Enter first release year: ")
            if not release_year.isdigit():
                print("Error: Release year must be a number.")
            else:
                break
    
        while True:
            num_pages = input("Enter number of pages: ")
            if not num_pages.isdigit():
                print("Error: Number of pages must be a number.")
            else:
                break
    
        book_info = f"{book_title},{author},{release_year},{num_pages}\n"

        self.file.seek(0)  
        books = self.file.readlines()

        for book in books:
            if book_info.strip() == book.strip():
                print("Error: This book already exists in the library.")
                return

        self.file.write(book_info)
        self.file.seek(0)  
        print("Book added successfully.")


    def remove_book(self, title):
        self.file.seek(0)  
        books = self.file.readlines()
        updated_books = []
        removed = False
        for book in books:
            if title in book:
                removed = True
            else:
                updated_books.append(book)
        
        if not removed:
            print("Book not found.")
            return
        
        self.file.seek(0)
        self.file.truncate()  
        for book in updated_books:
            self.file.write(book)
        print(f"Book {title} removed successfully")


lib = Library()


while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("q) Quit")

    choice = input("Please enter your choice: ")

    if choice == "1":
        print("Listing all books: ")
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        book_title_to_remove = input("Enter the title of the book to remove: ")
        lib.remove_book(book_title_to_remove)
    elif choice == "q" or "Q":
        print("Quitting...")
        break
    else:
        print("Invalid choice. Please choose again.")