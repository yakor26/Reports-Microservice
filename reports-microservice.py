from flask import Flask, request, jsonify
# temp holders 

#TODO 1: Generate counts of specific
app = Flask(__name__)
@app.route("/generate_count", methods=["POST"])
def generate_count():
    # request data and specific category need count for
    data = request.json
    category = data["category"]
    program_data = data["data"]

    # review all data submitted and add each of category to dictionary to keep count
    count = {}
    for row in program_data:
        if row[category] in count:
            count[row[category]] +=1
        else:
            count[row[category]] +=1


#TODO 2: Export Report as JSON, CSV
@app.route("/export", methods=["POST"])
def export_data():
    pass

# TODO 3: Filtered report based on selected filters 
@app.route("/filter", )
def temp():
    pass

if __name__ == "__main__":
    app.run(port=4000)

