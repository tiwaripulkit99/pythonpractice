student=()
name=(input("enter the name:"))
roll=int(input("enter the roll no:"))
marks=int(input("enter the marks:"))
student=name,roll,marks
print(student)
list1=list(student)
print(list1)
list1[2]=90
print(list1)
for i in list1:
    print(i)

