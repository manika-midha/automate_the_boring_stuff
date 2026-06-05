# means, match one or more
#the group preceding a plus must appear at least once. It is not optional.


import re

batregex = re.compile(r'bat(wo)+man')
mo = batregex.search('the adventures of batman')
if mo is not None :
    print(mo.group())
else :
    print ('None')

mo1 = batregex.search('the adventures of batwoman')
print(mo1.group())

mo2 = batregex.search('the adventures of batwowowoman')
print(mo2.group())