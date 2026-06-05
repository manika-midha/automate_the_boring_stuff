import re

phone_num_regex_obj = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})') #to search for () in regex , use a backlash with each bracket.\) \(
mo = phone_num_regex_obj.search('my number is (564) 674-8934')
if mo is None:
    print(f'no matching pattern found')
else :
    print(f'{mo.groups()}')

    