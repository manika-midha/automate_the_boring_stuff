
import re

#match any vowel - lowercase or uppercase
vowel_regex = re.compile(r'[aeiouAEIOU]')
print(vowel_regex.findall('the fox is crazy. the plants are green and fresh'))


#match all lowercase, uppercase, and digits and periods
all_regex = re.compile(r'[a-zA-Z0-9.]')
print(all_regex.findall('the FOX is crazy. The PLANTS are green and fresh. MY phone number is 678-908-1234'))

#caret character - negative characters, match all chars that are not vowels
c_regex = re.compile(r'[^ aeiouAEIOU]')
print(c_regex.findall('the FOX is crazy. The PLANTS are green and fresh. MY phone number is 678-908-1234'))