spam = ['apples', 'bananas', 'tofu', 'cats']

# def func(spam):
#     spam.insert(len(spam)-1, 'and')
#     #print(spam)
#     spam = ', '.join(spam)
#     spam = spam.replace('and,', 'and')
#     return spam 


# print(func(spam))

#print(func([]))

def func2():
    spam_str = ''
    for ind,wrd in enumerate(spam):
        if ind != len(spam)-1 :
            spam_str += f'{wrd}, ' 
        else:
            spam_str += f'and {wrd}'

    return spam_str 

print(func2())

def func3(spam):
    #spam_str = ', '.join(spam[0:-1]) + ', and ' + spam[-1]
    spam_str = f"{', '.join(spam[0:-1])}, and {spam[-1]}"
    return spam_str 

print(func3(spam))





