stuff = {'rope': 1 ,'torch': 6, 'gold coin' : 42 , 'dagger':1, 'arrow' : 12 }

def display(inventory):
    print('Inventory:')
    item_total = 0 
    #print count followed by item 
    for k,v in inventory.items():
        print(v,k) 
        item_total += v

    print(f'Total number of items is {item_total}')

display(stuff)