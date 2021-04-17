pos=-1
def search(list ,n):
    i=0
    while i<len(list):
       globals()['pos']=i
       if list[i]==n:
        return True
       i += 1
    return false


list=[1,2,67,45,334]
n=67
if search(list,n):
    print("found at",pos)
else:
    print("not found")