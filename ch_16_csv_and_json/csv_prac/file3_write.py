import csv

#op_file = open('output.csv', 'w', newline='')
op_file = open('output.csv', 'w')
op_writer = csv.writer(op_file)


for i in range(3):
    op_writer.writerow([f'hello{i}, world', f'eggs{i}', f'bacon{i}', f'ham{i}'])

op_file.close()