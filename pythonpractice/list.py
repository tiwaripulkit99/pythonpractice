'''list1=[1,2,3,4,5,6,7]
list2=[8,9,99,89,3,4,6]
list1.extend(list2)
print(list1)
newlist=[]
for item in list1:
    if item not in newlist:
       newlist.append(item)
print(newlist)
'''
list1=[1,2,3,4,5,6,7]
list2=[8,9,99,89,3,4,6]
list1.extend(list2)
print(list1)
n=set(list1)
print(n)