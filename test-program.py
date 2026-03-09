import requests

test_data = [
    {"title": "Pride and Prejudice", "author": "Jane Austen", "finished_date": "01/18/2026" , "pages": 430, "rating": 3, "genre": "romance"},
    {"title": "Dracula", "author": "Bram Stoker", "finished_date": "01/30/2026", "pages": 325, "rating": 4, "genre": "horror"},
    {"title": "Jane Eyre", "author": "Charlotte Brontë", "finished_date": "02/02/2026", "pages": 345, "rating": 2, "genre": "romance"},
    {"title": "1984", "author": "George Orwell", "finished_date": "02/08/2026", "pages": 416, "rating": 3, "genre": "science-fiction"}
]
# test_data = []
# test count based on category
def get_count_for_category():
# call generate count based on entered category
    category = "genre"
    try:
        response = requests.post("https://cs361-reports-microservice-production.up.railway.app/report/generate_count", json={"application_data": test_data, "category": category})
        response.raise_for_status()
        report = response.json()
    except requests.exceptions.RequestException as error:
        print(error)
    else:
        print(report)

# get filter by date
def get_filter_by_date():
# call generate count based on specific date column
    date_column = "finished_date"
    filter_columns = ["title", "author"]
    start_date = "01/30/2026"
    end_date = "02/07/2026"
    try:
        response = requests.post("https://cs361-reports-microservice-production.up.railway.app/report/filter_date", json={"application_data": test_data, "date_column": date_column, 
        "dates": {"start_date": start_date, "end_date": end_date}})
        report = response.json()
    except requests.exceptions.RequestException as error:
        print(error) 
    else:
        print(report)
        
# test stats 
def get_statistics():
    columns = ["pages", "rating"]
    try:
        response = requests.post("https://cs361-reports-microservice-production.up.railway.app/report/calculate_stats", json={"application_data": test_data, "columns": columns
        })
        report = response.json()
    except requests.exceptions.RequestException as error:
        print(error)
    else:
        print(report)
    
def main():
    # get_count_for_category()
    get_filter_by_date()
    # get_statistics()


    
if __name__ == "__main__":
    main()