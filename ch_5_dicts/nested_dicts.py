'''This func returns the fruits with their counts'''


allGuests = {
    'alice' : {'apples':5,'prets' :12},
    'bob' : {'sandwhiches':3, 'apples':2} ,
    'carol' : {'cups':3, 'pies':1 } ,
}

def brought(allGuests,fruits_key):
    fruit_count = 0 
    for k,v in allGuests.items():
        '''get method takes two arguments : the key of the value to retrieve and a fallback value 
        to return if the key does not exist'''
        fruit_count += v.get(fruits_key,0)
    return fruit_count


print(f"Apples brought - {brought(allGuests,'apples')}")
print(f"Prets brought - {brought(allGuests,'prets')}")
print(f"Sandwhiches brought - {brought(allGuests,'sandwiches')}")
print(f"Cups brought - {brought(allGuests,'cups')}")
print(f"Pies brought - {brought(allGuests,'pies')}")
print(f"Plates brought - {brought(allGuests,'plates')}")

