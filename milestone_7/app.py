from flask import Flask
from flask import request
from flask import jsonify
import csv

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/birthdays")
def birthday():
    # ?month=april&department=HR
    month = request.args.get('month', type = str)
    department = request.args.get('department', type = str)
    month_name_to_number = {
        'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12
    }
    month_num = month_name_to_number[month]
    result = {
        'eployees':[]
    }
    with open("database.csv", "r") as file:
        reader = csv.reader(file)
        id = 1
        for row in reader:
            if len(row) > 0:
                if row[3].find("." + str(month_num) + ".") != -1 and row[1] == department.lower():
                    data = {
                        "id": id,
                        "name": row[0],
                        "birthday": month.capitalize()+' '+row[3].split('.')[0]
                    }
                    id += 1
                    result["eployees"].append(data)

    result["total"] = len(result["eployees"])
    return jsonify(result)

@app.route("/anniversaries")
def anniversaries():
    # ?month=april&department=HR
    month = request.args.get('month', type = str)
    department = request.args.get('department', type = str)
    month_name_to_number = {
        'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12
    }
    month_num = month_name_to_number[month]
    result = {
        'eployees':[]
    }
    with open("database.csv", "r") as file:
        reader = csv.reader(file)
        id = 1
        for row in reader:
            if len(row) > 0:
                if row[2].find("." + str(month_num) + ".") != -1:
                    data = {
                        "id": id,
                        "name": row[0],
                        "birthday": month.capitalize()+' '+row[2].split('.')[0]
                    }
                    id += 1
                    result["eployees"].append(data)


    result["total"] = len(result["eployees"])
    return jsonify(result)



