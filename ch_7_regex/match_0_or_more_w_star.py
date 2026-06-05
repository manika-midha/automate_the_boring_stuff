#the star or asterisk means match 0 or more instances
#the group that precedes the star can occur any number of times in the text
#it can be completely absent or repeated over and over again

import re

batregex = re.compile(r'bat(wo)*man')
mo = batregex.search('the adventures of batman')
print(mo.group())

mo1 = batregex.search('the adventures of batwoman')
print(mo1.group())

mo2 = batregex.search('the adventures of batwowowoman')
print(mo2.group())