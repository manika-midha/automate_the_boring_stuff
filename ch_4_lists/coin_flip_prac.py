list1 = ['a','a','a','b','b','c','c','c','a','a','a']
list1_str = ''.join(list1)
print(list1_str)
pat1 = 'aaa'
pat2 = 'ccc'
st = 0

st = list1_str.count(pat1) + list1_str.count(pat2)

print(st)

