import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("month")
args = parser.parse_args()

month_name_to_number = {
    'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12
}

month = month_name_to_number[args.month]
result = {"Anniversaries":[], "Birthdays":[]}
with open("database.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) > 0:
            if row[2].find("." + str(month) + ".") != -1:
                result["Anniversaries"].append(row)
            if row[3].find("." + str(month) + ".") != -1:
                result["Birthdays"].append(row)

print(f"Report for {args.month.capitalize()} generated")
print("--- Birthdays ---")
print("Total: ", len(result["Birthdays"]))
print("By department:")
Birthdays_by_department = {}
for row in result["Birthdays"]:
    if row[1] in Birthdays_by_department.keys():
        Birthdays_by_department[row[1]]+=1
    else:
        Birthdays_by_department[row[1]]=1
for dep in Birthdays_by_department.keys():
    print(f"- {dep}: {Birthdays_by_department[dep]}")

print("--- Anniversaries ---")
print("Total: ", len(result["Anniversaries"]))
print("By department:")
Anniversaries_by_department = {}
for row in result["Anniversaries"]:
    if row[1] in Anniversaries_by_department.keys():
        Anniversaries_by_department[row[1]]+=1
    else:
        Anniversaries_by_department[row[1]]=1
for dep in Anniversaries_by_department.keys():
    print(f"- {dep}: {Anniversaries_by_department[dep]}")



