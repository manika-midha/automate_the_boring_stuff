import re

#search

search_reg_obj = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = search_reg_obj.search('my work number is 546-890-1234 and home number is 123-908-4567')
print(mo.group())


#find_all
findall_reg_obj = re.compile(r'\d{3}-\d{3}-\d{4}')
print(findall_reg_obj.findall('my work number is 546-890-1234 and home number is 123-908-4567'))


#find_all with groups
findall_g_reg_obj = re.compile(r'(\d{3})-(\d{3}-\d{4})')
print(findall_g_reg_obj.findall('my work number is 546-890-1234 and home number is 123-908-4567'))