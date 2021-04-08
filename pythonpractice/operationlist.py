list=[1,2,3,4,5,5]
print(list)
list[2] =95
print(list)
list.extend(["hello","elelel"])
print(list)
print(*list,sep = ", ")
if  "hello" in list:
    print("yes")
#change items from range
list[1:3]=["hi","bye",]
print(list)
list.insert(2,"byts")
print(list)
list.append("pulkit")
print(list)
newlist=["ye","nayi","list","hai"]
print(newlist)
list.extend(newlist)
print(list)

tuple=("ye" ,"tuple", "hai")
list.extend(tuple)
print(list)
list.remove("tuple")
print(list)
list.pop(2)
print(list)

[  print(i) for i in "pulkit"]
