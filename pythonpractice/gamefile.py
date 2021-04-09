
def game():
    return 40
score=game()
with open("hiscore.txt",'r')as f:
    hiscore=int(f.read())
    if hiscore<score:
       with open("hiscore.txt",'w')as f:
        f.write(str(score))
