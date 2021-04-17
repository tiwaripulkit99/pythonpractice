#at first normal program
"""def name(func):
    func("hi this is unique")
name(print) """
#now see what is decorating
def dec():
    def inner():
        return 4+5
    return inner
print(dec)