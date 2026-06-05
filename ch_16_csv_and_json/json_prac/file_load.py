import json

str_json_data = '{"name": "zophie", "is_cat": true, "mice_caught": 0, "feline_iq": null}'
json_as_py_data = json.loads(str_json_data)
print(json_as_py_data)
print(type(json_as_py_data))
