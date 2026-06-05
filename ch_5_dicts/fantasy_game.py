

def func(inventory, dragoon_loot):
    for x in dragoon_loot:
        inventory.setdefault(x, 0)
        inventory[x] += 1
    return inventory, sum(inventory.values())




inventory = {'gold_coin':42, 'rope':1}
dragoon_loot = ['gold_coin', 'dagger', 'gold_coin', 'gold_coin', 'ruby']

inv, cnt = func(inventory, dragoon_loot)

print(f"The inventory is {inv} and total loot is {cnt}")
