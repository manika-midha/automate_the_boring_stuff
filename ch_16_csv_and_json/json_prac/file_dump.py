import json

py_dict = {'name': 'zophie', 'is_cat': True, 'mice_caught': 0, 'feline_iq': None}
dict_str = json.dumps(py_dict)
print(dict_str)
print(type(dict_str))