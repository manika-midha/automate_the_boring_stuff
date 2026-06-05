import re 

tweetregex = re.compile (r'@(.*) ')
mo = tweetregex.search('haaaa@1234: 5hjyutren')
print(mo.group(1))