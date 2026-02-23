import requests

class Book:
    def __init__(self, bookID, title, finished_date, pages, rating):
        self._title = title,
        self._finished_date = finished_date,
        self._pages = pages,
        self._rating = rating


test_data = [
    {},
    {},
    {},
    {},
    {},
    {},
]


def prompt():
    book_title = input("Enter Book Title: ")
    book_author = input("Enter Author of Book: ")
    book_finished_date = input("Enter date book finished (mm/dd/yyyy): ")
    book_pages = input("Enter Number of Pages in Book: ")
    book_rating = input("Enter your Rating for the Book(1-5): ")


def main():
    pass



if __name__ == "__main__":
    main()

 
