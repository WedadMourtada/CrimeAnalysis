import csv

with open('./datasets/NYPD_Arrests_2020_2025.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)
    print(headers)
