
import random 

list_1 = ['h','t']
head_pat = 'hhhhhh'
tail_pat = 'tttttt'

def func(list_1,head_pat,tail_pat):
    streak = 0
    for x in range(10000):   
        count = 0  
        list_2 = [] 
        #create a list of 100 random values H or T.
        for i in range(100):
            list_2.append(random.choice(list_1))

        #check if there is a streak of 6 h or 6 t in a row.
        list_2_str = ''.join(list_2)
        count = list_2_str.count(head_pat) + list_2_str.count(tail_pat)
        streak = streak + count 
        
    return f'Chances of a streak happening are {(streak/10000)*100}%'
    
print(func(list_1,head_pat,tail_pat))
