# Reading a CSV file

import csv

# Reading CSV file


with open("data.txt", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)

