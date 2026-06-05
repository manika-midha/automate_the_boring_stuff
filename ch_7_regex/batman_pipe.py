import re

batRegex = re.compile(r'bat(man|mobile|cart|cream)')
mo = batRegex.search('batmobile is lost')
print(f'{mo.group()}')
print(f'{mo.groups()}')