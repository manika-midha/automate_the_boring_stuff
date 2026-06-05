import re 

input_str = 'My phone number is 675-907-8123'
def func(str_1):
    phone_num_regex_obj = re.compile(r'\d{3}-\d{3}-\d{4}')
    mo = phone_num_regex_obj.search(str_1)
    print(f'Number found is {mo.group()}')

print(func(input_str))