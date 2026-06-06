from myapp.models.book import Book

def instantiate_book() -> Book:
    title = input("Please enter the books title: ")
    author = input("Please enter the books author: ")
    return Book(title, author)

