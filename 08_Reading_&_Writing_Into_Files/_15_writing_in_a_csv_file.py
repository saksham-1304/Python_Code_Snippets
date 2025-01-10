import csv

# Writing a csv file
data = [["Name", "Age"], ["John", 30], ["Alice", 25], ["Bob", 35]]
with open("output3.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data)  # Writes all rows to the CSV file
