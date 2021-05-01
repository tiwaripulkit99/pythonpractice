"""a={1:"pulkit",2:"tiwari"}
list1=list(dict.keys(a))
list2=list(dict.values(a))

print(list1,list2)
d=dict(zip(list1,list2))
print(d)"""
"""set1={1,2,3}

set1.update([9,7,8])
print(set1)"""
'''str1="hyt this is pulki"
if "This".lower() in str1:
	print("hy")
print(str1.count("this"))
print("-".join(str1))
print(str1.find("this"))'''

"""def fun1(a):
	return a[2]
a=[[3,4,5],[90,80,70],[778,89,97]]
a.sort(key=fun1)
print(a)"""
"""list=[1,2,4,5]
for i in list:
	if i ==4:
	  print("found")
	  
else:
	print("not found")"""
"""  
list1=[1,2,3,4,5]
def search():
	return False
if search():
	print('hello')"""
list=[1,2,34,5453,4,34]
for index,values in enumerate(list,):
	print(index,values)