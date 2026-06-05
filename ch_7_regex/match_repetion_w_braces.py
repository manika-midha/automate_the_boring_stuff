'''
(ha){3} will match the string hahaha but not ha or haha
(ha){3,5} will match hahaha,hahahahaha,hahahahaha min 3, max 5
(ha){3,} will match minimum of 3 ha patterns - hahaha
(ha){,5} will match 0 to 5 instances
'''


import re

ha_regex = re.compile(r'(ha){3}') #match hahaha only
mo = ha_regex.search('ha is 1, haha is 2, hahaha is 3')
print(mo.group())

mo1 = ha_regex.search('ha is 1')
print(mo1)