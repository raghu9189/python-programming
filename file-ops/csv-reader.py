import csv

with open('file-ops/table.csv', encoding='utf-8', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

