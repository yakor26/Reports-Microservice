from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import statistics

app = FastAPI()
class CountReport(BaseModel):
    application_data: list
    category: str

    
#TODO 1: Generate counts of specific requested category
# @app.route("/generate_count", methods=["POST"])
# def generate_count():
#     # request data and specific category need count for
#     data = request.json
#     category = data["category"]
#     program_data = data["application_data"]

@app.post("/generate_count")
def generate_count(report: CountReport):
    # request data and specific category need count for
    category = report.category
    program_data = report.application_data

    # review all data submitted and add each of category to dictionary to keep count
    count = {}
    for row in program_data:
        if row[category] in count:
            count[row[category]] +=1
        else:
            count[row[category]] = 1
    # return count
    # format report
    formatted_report = {
        "report_type": f"category report - {category}",
        "created_at": datetime.now(),
        "data": count,
        "total_submitted": len(program_data)
    }
    return formatted_report


#TODO 2: Calculate stats and get statistical insights on data
# @app.route("/calculate_stats", methods=["POST"])
# def calculate_statistics():
#     data = request.json
#     program_data = data["application_data"]
#     # need to specific columns and they have to be numbers 
#     columns = data["columns"]
#     stats = {}
#     # for each selected column
#     for column in columns:
#         column_values = []
#         for row in program_data:
#             column_values.append(int(row[column]))
#         # calc
#         calculated_stats = {
#         "total" : sum(column_values),
#         "average": statistics.mean(column_values),
#         "max": max(column_values),
#         "min": min(column_values),
#         "median": statistics.median(column_values),
#         "mode":statistics.mode(column_values)
#         }
#         stats[column] = calculated_stats

#     formatted_report = {
#         "report_type": f"stats report",
#         "created_at": datetime.now(),
#         "data": stats,
#     }
#     return formatted_report

@app.post("/calculate_stats")
def calculate_statistics():
    data = request.json
    program_data = data["application_data"]
    # need to specific columns and they have to be numbers 
    columns = data["columns"]
    stats = {}
    # for each selected column
    for column in columns:
        column_values = []
        for row in program_data:
            column_values.append(int(row[column]))
        # calc
        calculated_stats = {
        "total" : sum(column_values),
        "average": statistics.mean(column_values),
        "max": max(column_values),
        "min": min(column_values),
        "median": statistics.median(column_values),
        "mode":statistics.mode(column_values)
        }
        stats[column] = calculated_stats

    formatted_report = {
        "report_type": f"stats report",
        "created_at": datetime.now(),
        "data": stats,
    }
    return formatted_report



# TODO 3: Filtered report based on selected filters 
@app.route("/filter_date", methods=["POST"])
def filter_by_date():
    # request data and grab start date and end date
    filtered_data = []
    data = request.json
    start_date = datetime.strptime(data["dates"]["start_date"], "%m/%d/%Y")
    end_date = datetime.strptime(data["dates"]["end_date"], "%m/%d/%Y")
    date_column = data["date_column"]
    program_data = data["application_data"]

    for row in program_data:
    # return filtered data within date range
        row_date = datetime.strptime(row[date_column], "%m/%d/%Y")
        if row_date >= start_date and row_date <= end_date:
            if "filter_columns" in data:
                requested_columns = data["filter_columns"]
                # store in new dict
                filtered_cols_data = {}
                for column in requested_columns:
                    filtered_cols_data[column] = row[column]
                filtered_data.append(filtered_cols_data)
            
            else:
                filtered_data.append(row)
    
    formatted_report = {
        "report_type": f"date range report from {start_date} - {end_date}",
        "created_at": datetime.now(),
        "data": filtered_data,
        "total_submitted": len(program_data),  
        "total_found": len(filtered_data)
    }
    return formatted_report
    

