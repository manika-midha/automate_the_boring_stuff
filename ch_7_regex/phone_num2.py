import re 

re_obj = re.compile(r'\d{3}-\d{3}-\d{4}')
match_obj = re_obj.search("My phone num is 476-900-9067")
print(match_obj.group())