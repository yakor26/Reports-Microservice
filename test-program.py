import requests


test_data = [
    {"title": "Pride and Prejudice", "author": "Jane Austen", "finished date": "01/02/2026" , "pages": 430, "rating": 3, "genre": "romance"},
    {"title": "Dracula", "author": "Bram Stoker", "finished date": "01/02/2026", "pages": 325, "rating": 4, "genre": "horror"},
    {"title": "Jane Eyre", "author": "Charlotte Brontë", "finished date": "01/02/2026", "pages": 345, "rating": 2, "genre": "romance"},
    {"title": "1984", "author": "George Orwell", "finished date": "01/02/2026", "pages": 416, "rating": 3, "genre": "science-fiction"}
]

def prompt():
    # basic prompt for book data
    test_count +=1
    book_title = input("Enter Book Title: ")
    book_author = input("Enter Author of Book: ")
    book_finished_date = input("Enter date book finished (mm/dd/yyyy): ")
    book_pages = input("Enter Number of Pages in Book: ")
    book_rating = input("Enter your Rating for the Book(1-5): ")
    # generate book object and add to test data
    # Book(book_title, book_author, book_finished_date, book_pages, book_rating)
    test_data.append({
        "title": book_title,
        "author": book_author,
        "finished date": book_finished_date,
        "pages": book_pages,
        "rating": book_rating
    })
    print("Added book to data\n")
    print(test_data)

    

def main():
    prompt()
    


if __name__ == "__main__":
    main()