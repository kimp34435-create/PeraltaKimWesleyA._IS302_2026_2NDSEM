class Book_kwap:
    def __init__(self_kwap, title_kwap, author_kwap, year_kwap):
        self_kwap.title_kwap = title_kwap
        self_kwap.author_kwap = author_kwap
        self_kwap.year_kwap = year_kwap
    
    def display_book_kwap(self_kwap):
        print("Title:", self_kwap.title_kwap)
        print("Author:", self_kwap.author_kwap)
        print("Year:", self_kwap.year_kwap)
        print()


print("----- LIBRARY MANAGEMENT SYSTEM -----\n")

# Create three book objects
book1_kwap = Book_kwap("Python Programming", "John Smith", 2022)
book2_kwap = Book_kwap("Data Science Basics", "Sarah Johnson", 2021)
book3_kwap = Book_kwap("Web Development Guide", "Mike Davis", 2023)

# Display book information
print("Book 1:")
book1_kwap.display_book_kwap()

print("Book 2:")
book2_kwap.display_book_kwap()

print("Book 3:")
book3_kwap.display_book_kwap()
