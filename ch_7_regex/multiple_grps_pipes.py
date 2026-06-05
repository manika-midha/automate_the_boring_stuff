import re


#if both texts are present, first matching text will be returned
regex_obj = re.compile(r'batman | tina fey') #look for batman or tina frey
#mo = regex_obj.search('my name is batman and not tina fey')
mo = regex_obj.search('my name is tina fey and not batman')
print(mo.group())