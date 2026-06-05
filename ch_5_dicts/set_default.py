'''this code prints the count of each character in the message string'''
message = "It was a beautiful Sunday. It would be nice to have days like these every now and then"
dict_char = {}

count = 0 
for ch in message :
    '''set a value for a key only if it does not have a value (key does not exist)'''
    '''first argument in setdefault() is the key to check for, second argument is the 
    value to set at that key if the key does not exist.'''
    count = dict_char.setdefault(ch,0)
    count += 1
    dict_char[ch] = count 

print(dict_char)