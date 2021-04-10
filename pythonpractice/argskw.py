#use of args fucntion
"""def funargs(*args):
    for item in args:
        print(item)

name="pulkit","joh","rock","rocky"
funargs(*name)"""
#use of kwargs:
def funargs(*args,**kwargs):
    for item in args:
        print(item)
    for key,value in kwargs.items():
        print(key,value)

name=["pulkit","john","rock","rocky"]
sir={"tiwari":"cena","salam":"bhai"}
funargs(*name,**sir)


