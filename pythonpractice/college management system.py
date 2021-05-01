class college:
    def __init__(self,clg_name):
        self.clg_name=clg_name
        print(f"'Hy welcome to our college'-{self.clg_name}")
    def admission(self):
        self.fee_BCA_="Rs50000"
        self.fee_MCA="Rs100k"
        self.fee_Btech="Rs80k"
        print(f"The fee structure is { self.fee_BCA_} for BCA")
        print(f"The fee structure is {self.fee_MCA} for MCA")
        print(f"The fee structure is {self.fee_Btech} for B.tech")
    def faculties(self):
        self.Ds="Ritesh"
        self.Python="Aswathi"
        self.Java="Pratibha"
        print(f"our faculty for DS is {self.Ds }")
        print(f"our faculty for Python is {self.Python} ")
        print(f"our faculty for Java is {self.Java}")
    def eligibility(self):
        self.Per_10="75%"
        self.Per_12="80%"
        print(f"The percentage criteria is {self.Per_10} for 10th And {self.Per_12} for 12th")
ob=college("Mahankal Institute of Tecno And Management")
while(True):
    print("Menu---")
    print("press 1 to see our Fee structure")
    print("press 2 to see our Faculties")
    print("press 3 to see our Admission eligibilty")
    choice=int(input())
    if choice==1:
        ob.admission()
    elif choice==2:
        ob.faculties()
    elif choice==3:
        ob.eligibility()
    else :
        print("Enter the valid choice:")
    print("Press q to quit and c to continue")
    userchoice2 = ""
    while (userchoice2 != "c" and userchoice2 != "q"):
        userchoice2 = input()
        if userchoice2 == "q":
            exit()
        if userchoice2 == "c":
            continue

