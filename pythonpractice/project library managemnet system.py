class library:
    def __init__(self,booklist,name):
        self.name=name
        self.booklist=booklist
        self.lenddict={}
    def displaybook(self):
        print(f"We have following books in our library:{self.name}")
        for book in self.booklist:
            print(book)
    def lendbook(self,user,book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print("Lender book database has been updated.You can take the book now")
        else :
            print(f"Book is already being used by {self.lenddict[book]}")
    def addbook(self,book):
        self.booklist.append(book)
        print("Book has been added to booklist")
    def returnbook(self,book):
        self.lenddict.pop(book)
if __name__ == '__main__':
        pulkit=library(["python","richdaddypoordaddy","harrypotter","c++","algo"],"Codewithpulkit")

        while(True):
            print(f"Welcome to the {pulkit.name} library.Enter your choice to continue")
            print("1.DisplayBooks")
            print("2.lend a Book")
            print("3.Add a Book")
            print("4.Return a Book")
            userchoice=int(input())
            if userchoice==1:
                pulkit.displaybook()
            elif userchoice==2:
                book=input("Enter the Bookname you want to lend")
                user=input("Enter your Name")
                pulkit.lendbook(user,book)
            elif userchoice == 3:
                book=input("Enter the Bookname you want to add")
                pulkit.addbook(book)
            elif userchoice == 4:
                book = input("Enter the Bookname you want to return")
                if book not in pulkit.lenddict:
                    print("It's already in our library!Give a valid book!")
                else:pulkit.returnbook(book)
            else:
                print("Please select a valid option!")
            print("Press q to quit and c to continue")
            userchoice2=""
            while(userchoice2!="c" and userchoice2!="q"):
             userchoice2=input()
             if userchoice2=="q":
                 exit()
             if userchoice2=="c":
                 continue