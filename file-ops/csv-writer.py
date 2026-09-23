import csv

with open('file-ops/table-two.csv', encoding='utf-8', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow([1, 'A', 20])

