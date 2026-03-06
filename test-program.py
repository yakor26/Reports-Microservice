import requests

test_data = [
    {"title": "Pride and Prejudice", "author": "Jane Austen", "finished_date": "01/18/2026" , "pages": 430, "rating": 3, "genre": "romance"},
    {"title": "Dracula", "author": "Bram Stoker", "finished_date": "01/30/2026", "pages": 325, "rating": 4, "genre": "horror"},
    {"title": "Jane Eyre", "author": "Charlotte Brontë", "finished_date": "02/02/2026", "pages": 345, "rating": 2, "genre": "romance"},
    {"title": "1984", "author": "George Orwell", "finished_date": "02/08/2026", "pages": 416, "rating": 3, "genre": "science-fiction"}
]
# test count based on category
def get_count_for_category():
# call generate count based on entered category
    category = "genre"
    response = requests.post("http://127.0.0.1:8005/generate_count", json={"application_data": test_data, "category": category})
    if response.status_code == 200:
        report = response.json()
        print(report)
        # print(f"Report for Book {category.title()}: ") 
        # for row in report: 
        #     print(f'{row.title()} - {int(report[row])}')
    else:
        return "Failed to generate category report data"
# get filter by date
def get_filter_by_date():
# call generate count based on specific date column
    date_column = "finished_date"
    filter_columns = ["title", "author"]
    start_date = "01/30/2026"
    end_date = "02/07/2026"
    response = requests.post("http://127.0.0.1:8005/filter_date", json={"application_data": test_data, "date_column": date_column, 
    "dates": {"start_date": start_date, "end_date": end_date}})
    if response.status_code == 200:
        report = response.json()
        print(report)
        # print(f"Books within {start_date} - {end_date}: ") 
        # for row in report: 
        #     print(row)
    else:
        return "Failed to find dates within specified date range"

# test stats 
def get_statistics():
    columns = ["rating", "pages"]
    response = requests.post("http://127.0.0.1:8005/calculate_stats", json={"application_data": test_data, "columns": columns
    })
    if response.status_code == 200:
        report = response.json()
        print(report)
        
    else:
        return "Failed to get statistics from data"
    
def main():
    # get_count_for_category()
    # get_filter_by_date()
    get_statistics()


    
if __name__ == "__main__":
    main()