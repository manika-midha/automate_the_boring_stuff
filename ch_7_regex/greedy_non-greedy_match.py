import re

#by default, you will get the longest string
greedy_reg_obj = re.compile(r'(ha){3,5}')
mo = greedy_reg_obj.search('hahahahaha')
print(mo.group())


#add ? and you will get the shortest string
nongreedy_reg_obj = re.compile(r'(ha){3,5}?')
mo1 = nongreedy_reg_obj.search('hahahahaha')
print(mo1.group())