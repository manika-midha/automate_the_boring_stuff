import re

#to make your regex case insensitive, pass re.I as the second argument in re.compile
robocop = re.compile('robocop',re.I)
print(robocop.search('RoboCop is for real').group())
print(robocop.search('Robocop is for real').group())
print(robocop.search('robocop is for real').group())