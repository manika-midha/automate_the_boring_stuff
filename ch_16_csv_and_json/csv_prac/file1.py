import csv

eg_file = open('example.csv')
eg_reader = csv.reader(eg_file)  # reader object
eg_data = list(eg_reader)

print(eg_data)