# the ? character flags the group () that precedes it as an optional part of the pattern
# ? means , match 0 or one of the group preceding this question mark

import re

phone_regex = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
mo = phone_regex.search('my number is 456-908-1267')
print(mo.group())

mo1 = phone_regex.search('my number is 908-1267')
print(mo1.group())