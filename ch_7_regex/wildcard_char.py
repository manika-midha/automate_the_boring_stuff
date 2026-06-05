import re 

# .(dot) character in a regular expression is called a wildcard and will match any single character except the newline character
at_regex = re.compile(r'.at')
print(at_regex.findall('the cat is bat crazy but her hat is afate \nat'))
#print(at_regex.findall('the cat is bat crazy but her hat is afate.\nthe mat is not baat cate'))

#match anything with dot star (.*)
# . means any single character except the newline
# * means 0 or more occurences of the preceding character
# .* uses greedy mode, it tries to match as much as text as possible.
name_regex = re.compile(r'first name: (.*) last name: (.*)') 
mo = name_regex.search('first name: harry and last name: potter')
print(mo.group(1))
print(mo.group(2))
