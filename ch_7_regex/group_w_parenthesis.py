import re

#parenthesis divides in groups. The number of groups starts from1
phone_num_regex_obj = re.compile(r'(\d{3})-(\d{3}-\d{4})') 
mo = phone_num_regex_obj.search('my number is 413-908-1278')
print(f'{mo.group()}')
print(f'{mo.groups()}') #returns a tuple of different groups
print(f'{mo.group(1)}')
print(f'{mo.group(2)}')

area_code, main_num = mo.groups()
print(f'the area code is {area_code}')
print(f'the main number is {main_num}')