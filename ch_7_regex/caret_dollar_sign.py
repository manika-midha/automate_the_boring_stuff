import re

#1
# use ^ at the start of a regex to indicate that a match must occur at the start of a searched text
hello_regex = re.compile(r'^Hello')
print(hello_regex.search('Hello, my name is tommy'))

#as hello is at end, no match
print(hello_regex.search('My name is tommy, Hello'))

#2
#use $ at the end of the regex to indicate the string must end with the regex
hello_regex = re.compile(r'Hello$')
print(hello_regex.search('Hello, my name is tommy'))

print(hello_regex.search('My name is tommy, Hello'))

#3
#use ^ and $ together the complete string
digit_regex = re.compile(r'^\d+$') #the string should start and end with one or more digit
print(digit_regex.search('12458976'))
print(digit_regex.search('124  58976'))
print(digit_regex.search('x12458976'))