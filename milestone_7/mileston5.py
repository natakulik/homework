import random

name = ['Konstantin', 'Nataliia', 'Viktoriia', 'Oksana', 'Ruslan']
department = ['service', 'sales', 'management']
hiring_date = [2010, 2012, 2012, 2014, 2015]
birthday = [1995, 1991, 1996, 1982, 1974]

test_data = []

for i in range(100):
    row = {
        'name': name[random.randint(0, len(name) - 1)],
        'department': department[random.randint(0, len(department) - 1)],
        'hiring_date': str(random.randint(1, 28)) + '.' + str(random.randint(1, 12)) + '.' + str(
            hiring_date[random.randint(0, len(hiring_date) - 1)]),
        'birthday': str(random.randint(1, 28)) + '.' + str(random.randint(1, 12)) + '.' + str(
            birthday[random.randint(0, len(birthday) - 1)]),
    }
    test_data.append(row)



print( test_data )

import csv


with open('database.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=list(test_data[0].keys()))
    writer.writeheader()
    for row in test_data:
        writer.writerow(row)

with open('database.csv') as file:
    print(file.read())