#add new item before last item in a list and return the list as a string

spam = ['apples', 'bananas', 'tofu', 'cats']
spam.insert(len(spam)-1, 'and ')
print(spam)
print(' '.join(spam))

output = 'apples,bananas,tofu, and cats'

