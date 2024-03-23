import csv
import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("month")
parser.add_argument("department")

args = parser.parse_args()

month_name_to_number = {
    'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12
}

month = month_name_to_number[args.month]
department = args.department
url = f'http://127.0.0.1:5000/birthdays?month={args.month.lower()}&department={args.department.lower()}'
data = requests.get(url)

print(f'Report for {args.department.capitalize()} department for {args.month.capitalize()} fetched.')
print('Birthdays')
print(f'Total: {data.json()['total']}')
print('Employees:')
for emp  in data.json()['eployees']:
    print(f'- {emp['birthday']}, {emp['name']}')

url = f'http://127.0.0.1:5000/anniversaries?month={args.month.lower()}&department={args.department.lower()}'
data = requests.get(url)

print()
print('---------------------------')
print()
print('Anniversaries')
print(f'Total: {data.json()['total']}')
print('Employees:')
for emp  in data.json()['eployees']:
    print(f'- {emp['birthday']}, {emp['name']}')