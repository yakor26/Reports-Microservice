import requests

# class Book:
#     def __init__(self, title, author, finished_date, pages, rating):
#         self._title = title,
#         self._author = author
#         self._finished_date = finished_date,
#         self._pages = pages,
#         self._rating = rating

test_data = []

def main():
    # basic prompt for book data
    test_count = 0
    while test_count < 4:
        test_count +=1
        book_title = input("Enter Book Title: ")
        book_author = input("Enter Author of Book: ")
        book_finished_date = input("Enter date book finished (mm/dd/yyyy): ")
        book_pages = input("Enter Number of Pages in Book: ")
        book_rating = input("Enter your Rating for the Book(1-5): ")
        # generate book object and add to test data
        Book(book_title, book_author, book_finished_date, book_pages, book_rating)
        test_data.append({
            "title": book_title,
            "author": book_author,
            "finished date": book_finished_date,
            "pages": book_pages,
            "rating": book_rating
        })
        print("Added book to data\n")
        print(test_data)


if __name__ == "__main__":
    main()