dragon_list = ['gold coin', 'dagger','gold coin','gold coin', 'ruby']
inventory = {'gold coin': 42, 'rope' : 1}

def addtoInventory(inventory,dragon_list):
    for val in dragon_list:
        inventory.setdefault(val,0) #if val exists, set its value to 0
        inventory[val] += 1 #if key/val exists already, increase the existng val by 1
    return inventory

y = addtoInventory(inventory, dragon_list)
print(y)