# install a external  module of your interest and use it.
"""from playsound import playsound
playsound('testing.mp3') """
#write amprogram to print content of directory using os module
"""import os
print(os.listdir())"""
#write of program of type casting
"""a="3434"
print(type(a))
a=int(a)
print(a)
print(type(a))"""
#program to finf average of 2 nmber enterd by the user:
"""n1=int(input("enter no.1:"))
n2=int(input("enter no.2:"))
average=(n1+n2)/2
print("the average of%d"%n1,"and %d"%n2,"is",average)"""
#string trial
"""name="pulkit tiwari is boy"
print(name[0:6])"""
#program to filled details in letter using name and date ,taking it from user:
"""letter=''' hello <|name>,
happy to share you this greetings hat you have been selected  !
date:<|date>'''
name=(input("enter name:"))
date=(input("enter the date:"))
letter=letter.replace("<|date>",date)
letter=letter.replace("<|name>",name)
print(letter.endswith(date))
print(letter) 
"""
""" program to detect double spaces in the string
 list programs"""
"""list=[1,2,3,4]
print(list.pop())"""
"""marks1=int(input("enter the marks1:"))
marks2=int(input("enter the marks2:"))
marks3=int(input("enter the marks3:"))
marks4=int(input("enter the marks4:"))
list=[marks1,marks2,marks3,marks4]
list.sort()
print(list)"""
"""listnew=0
for i in range(0,len(list)):
   listnew=list[i]+listnew
print(listnew)
print(list)"""
"""set1={1,2,3,4,4,3,6,7,8,9.00}
set2={2,9,90,}
print(set1.intersection(set2))"""
set={1,2,3,4.00,4,"4"}
print(set)