import csv

csv_file = open('example.tsv', 'w', newline='')
csv_writer = csv.writer(csv_file, delimiter='\t', lineterminator='\n\n')

for i in range(3):
    csv_writer.writerow([f'hello{i}, world', f'spam{i}', f'bacon{i}', f'eggs{i}'])