# map_reduce_demo.py
import csv
from collections import defaultdict

def map_reduce_arrests(file_path):
    borough_counts = defaultdict(int)
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            borough = row['ARREST_BORO']  
            borough_counts[borough] += 1
    return borough_counts

if __name__ == "__main__":
    file_path = './datasets/NYPD_Arrests_2020_2025.csv'
    result = map_reduce_arrests(file_path)
    print("MapReduce Arrest Counts Per Borough (2020-2025 Data):")
    for borough, count in result.items():
        print(f"{borough}: {count}")
