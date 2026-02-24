import requests


test_data = [
    {"title": "Pride and Prejudice", "author": "Jane Austen", "finished_date": "01/18/2026" , "pages": 430, "rating": 3, "genre": "romance"},
    {"title": "Dracula", "author": "Bram Stoker", "finished_date": "01/30/2026", "pages": 325, "rating": 4, "genre": "horror"},
    {"title": "Jane Eyre", "author": "Charlotte Brontë", "finished_date": "02/02/2026", "pages": 345, "rating": 2, "genre": "romance"},
    {"title": "1984", "author": "George Orwell", "finished_date": "02/08/2026", "pages": 416, "rating": 3, "genre": "science-fiction"}
]

def main():
    # # basic prompt for book data
    # book_title = input("Enter Book Title: ")
    # book_author = input("Enter Author of Book: ")
    # book_finished_date = input("Enter date book finished (mm/dd/yyyy): ")
    # book_pages = input("Enter Number of Pages in Book: ")
    # book_rating = input("Enter your Rating for the Book(1-5): ")
    # book_genre = input("Enter Book Genre: ")
    # # generate book object and add to test data
    # # Book(book_title, book_author, book_finished_date, book_pages, book_rating)
    # test_data.append({
    #     "title": book_title,
    #     "author": book_author,
    #     "finished date": book_finished_date,
    #     "pages": book_pages,
    #     "rating": book_rating,
    #     "genre": book_genre
    # })
    # # debug statements
    # print("Added book to data\n")
    # print(test_data)
    get_count_for_category()


    def get_count_for_category():
    # call generate count based on entered category
        category = "genre"
        response = requests.post("http://localhost:4000/generate_count", json={"application_data": test_data, "category": category})
        if response.status_code == 200:
            report = response.json()
            print(f"Report for {category.title()}: ") 
            for row in report: 
                print(f'{row.title()} - {int(report[row])}')
        else:
            return "Failed to generate category report data"
    
    def get_count_for_category():
    # call generate count based on specific date column
        date_column = "finished_date"
        start_date = "01/30/2026"
        end_date = "02/07/2026"
        response = requests.post("http://localhost:4000/filter_date", json={"application_data": test_data, "date_column": date_column,
        "dates": {"start_date": start_date, "end_date": end_date}})
        if response.status_code == 200:
            report = response.json()
            print(f"Data within {start_date} - {end_date}: ") 
            for row in report: 
                print(row)
        else:
            return "Failed to find dates within specified date range"

    
if __name__ == "__main__":
    main()