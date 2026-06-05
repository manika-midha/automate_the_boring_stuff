import csv

eg_file = open('exampleWithHeader.csv')
eg_dict_reader = csv.DictReader(eg_file)

for row in eg_dict_reader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])

    