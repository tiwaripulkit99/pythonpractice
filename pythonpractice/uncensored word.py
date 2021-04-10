words=["donkey","chutia","bewkuf"]
with open("uncensor.txt",'r') as f:
    content= f.read()
for word in words:
     content=content.replace(word,"$$**$$") 
     with open("uncensor.txt",'w') as f:
        f.write(content)
      