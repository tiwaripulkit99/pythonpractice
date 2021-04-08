"""print("list of list")
nums=[10,20,30]
values=[100000,6000,[1,2,3]]
data=[1200,9000,]
mainlist=[nums,data,values]

print(min(mainlist))
print(max(mainlist))"""
'''list1=[5,6,7,[8,9,[12,34]]]
list1[0]=100
print(list1)
list1[3][2][1]=56
print(list1)
'''
list12=[3,4,5,6,6,7,7]
list13=[ i for i in list12 if list12.count(i)>1]
print(list13)