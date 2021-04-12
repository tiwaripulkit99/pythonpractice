# use of map be like
"""num=[1,2,3,4,5]
square=list(map(lambda x:x*x,num))
print(square)"""
# use of filter function
"""list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def is5(num):
    return num > 5
print(list(filter(is5, list1)))"""
#use if reduce fucntion
from functools import reduce
num=[1,2,3,4,5,6]
print(reduce(lambda x,y:x+y,num))
