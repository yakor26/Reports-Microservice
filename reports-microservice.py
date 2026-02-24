from flask import Flask, request
from datetime import datetime
# temp holders 

#TODO 1: Generate counts of specific requested category
app = Flask(__name__)
@app.route("/generate_count", methods=["POST"])
def generate_count():
    # request data and specific category need count for
    data = request.json
    category = data["category"]
    program_data = data["application_data"]

    # review all data submitted and add each of category to dictionary to keep count
    count = {}
    for row in program_data:
        if row[category] in count:
            count[row[category]] +=1
        else:
            count[row[category]] = 1
    # return count
    return count


#TODO 2: Export Report as JSON, CSV
@app.route("/export", methods=["POST"])
def export_data():
    pass

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
            filtered_data.append(row)
    return filtered_data
    

if __name__ == "__main__":
    app.run(port=4000)
