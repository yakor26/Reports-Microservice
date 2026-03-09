from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import statistics

app = FastAPI()
# model for count report
class CountReport(BaseModel):
    application_data: list
    category: str

# stats report
class StatisticsReport(BaseModel):
    application_data: list
    columns: list


# dates dictionary
class SpecificDates(BaseModel):
    start_date: str
    end_date: str

# 
class DateReport(BaseModel):
    application_data: list
    date_column: str
    dates: SpecificDates
    filter_columns: list | None = None


    
#TODO 1: Generate counts of specific requested category
@app.post("/report/generate_count")
def generate_count(report: CountReport):
    # request data and specific category need count for
    category = report.category
    program_data = report.application_data

    # review all data submitted and add each of category to dictionary to keep count
    count = {}
    # validate data is provided
    if not program_data:
        raise HTTPException(status_code=400, detail="No data was provided for category report")
        
    for row in program_data:
        if category not in row:
            continue
        else:
            if row[category] in count:
                count[row[category]] +=1
            else:
                count[row[category]] = 1

    # validate category provided exists after checking all rows
    if not count:
        raise HTTPException(status_code=400, detail="category provided does not exist")
    # format report
    formatted_report = {
        "report_type": f"category report - {category}",
        "created_at": datetime.now(),
        "data": count,
        "total_submitted": len(program_data)    
        }
    return formatted_report


@app.post("/report/calculate_stats")
def calculate_statistics(report: StatisticsReport):
    program_data = report.application_data
    # validate data is provided
    if not program_data:
        raise HTTPException(status_code=400, detail="No data was provided for statistics report")
    # need to specific columns and they have to be numbers 
    columns = report.columns
    # validate column provided 
    if not columns:
        raise HTTPException(status_code=400, detail="column for statistics was not provided")
    stats = {}
    # for each selected column
    for column in columns:
        column_values = []
        for row in program_data:
            # TODO add error handling for non numeric input columns
            if column not in row:
                continue
            try: 
                value = float(row[column])
            # for columns that have non numeric values end immediately
            except ValueError:
                raise HTTPException(status_code=400, detail="column contains non numeric values")     
            column_values.append(value)
        
        # check that columns were valid, check anything was added
        if not column_values:
            raise HTTPException(status_code=400, detail="column for statistics provided does not exist")
        # calc
        calculated_stats = {
        "total" : sum(column_values),
        "average": statistics.mean(column_values),
        "max": max(column_values),
        "min": min(column_values),
        "median": statistics.median(column_values)
        }
        stats[column] = calculated_stats

    formatted_report = {
        "report_type": f"stats report",
        "created_at": datetime.now(),
        "data": stats,
    }
    return formatted_report


# TODO 3: Filtered report based on selected filters 
@app.post("/report/filter_date")
def filter_by_date(report: DateReport):
    # request data and grab start date and end date
    filtered_data = []
    try:
        start_date = datetime.strptime(report.dates.start_date, "%m/%d/%Y")
        end_date = datetime.strptime(report.dates.end_date, "%m/%d/%Y")
    except ValueError:
        raise HTTPException(status_code=400, detail="date format incorrect, format should be mm/dd/yyyy")
    date_column = report.date_column
    # error handling for date column
    if not date_column:
        raise HTTPException(status_code=400, detail="No data was provided for column to use for date")
    program_data = report.application_data
    # error handling for data
    if not program_data:
        raise HTTPException(status_code=400, detail="No data was provided for filter by date report")

    for row in program_data:
    # return filtered data within date range
        try:
            row_date = datetime.strptime(row[date_column], "%m/%d/%Y")
        except ValueError:
            continue
        if row_date >= start_date and row_date <= end_date:
            if report.filter_columns is not None:
                requested_columns = report.filter_columns
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
    

