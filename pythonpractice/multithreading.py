"""from threading import *
class Hello(Thread):

    def run(self):
        import time
        for i in range(5):
            print("HEllo")
            time.sleep(3)


class Hii(Thread):
    def run(self):
        for i in range(5):
            print("Hii")
t1=Hello()
t2=Hii()
t1.start()
t2.start()
t1.join()
t1.join()
print("bye")"""
