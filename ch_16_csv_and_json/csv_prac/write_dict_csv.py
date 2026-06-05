import csv

op_file = open('output_dict.csv', 'w', newline='')
op_dict_writer = csv.DictWriter(op_file, ['Name', 'Pet', 'Phone'])
op_dict_writer.writeheader()


for i in range(3):
    op_dict_writer.writerow(
        {
            'Name': f'Harry{i}',
            'Pet': f'Bird{i}',
            'Phone': f'Phone{i}'
        }
    )

op_file.close()
