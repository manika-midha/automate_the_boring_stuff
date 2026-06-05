all_guests = {
    'alice' : {'apples':5,'prets' :12},
    'bob' : {'sandwhiches':3, 'apples':2} ,
    'carol' : {'cups':3, 'pies':1 } ,
}

def func(all_guests):
    result_dict = {}
    #vals_keys_set = set()
    for val_dict in all_guests.values():
        for ky, val in val_dict.items():
            #vals_keys_set.add(ky)
            result_dict.setdefault(ky, 0)
            result_dict[ky] += val

    return result_dict

main_dict = func(all_guests)
print(main_dict)
result_str = "The guests bought: "
for k, v in main_dict.items():
    result_str += str(v) + ' ' + k + ', '

print(result_str)

