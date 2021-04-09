#to read the file
""" 
f = open("sample.txt",'r')
data=f.read()
print(data)
f.close """
#to read the file using readlione function:
"""f = open("sample.txt",'r')
data=f.readline()
 
print(data)
data=f.readline()
print(data)

f.close
"""
#writing in a file:
"""f=open('another.txt','w')
f.write("hello this is another file")
f.close"""
#appending in a  file:
"""f=open('another.txt','a')
f.write("hello this is another file and i am appending in it")
f.close
f=open('another.txt','r')
data=f.read()
print(data)
f.close
"""
#to check if any word in present in the file or not
"""f=open("poem.txt",'r')
poem=f.read()
f.close
if "twinkle" in poem:
    print("yes it is present")
else:
    print("not present")"""

def game():
    return 40
score=game()
with open("hiscore.txt",'r')as f:
    hiscore=int(f.read())
    if hiscore<score:
       with open("hiscore.txt",'w')as f:
        f.write(str(score))

