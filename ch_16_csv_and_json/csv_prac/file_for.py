import csv

eg_file = open('example.csv')
eg_reader = csv.reader(eg_file)

for row in eg_reader:
    print(f"Row #{eg_reader.line_num} {row}")
