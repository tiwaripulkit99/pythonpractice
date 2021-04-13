import time
from functools import lru_cache
@lru_cache(maxsize=3)#last 3
def check(n):
    time.sleep(n)
    return
check(5)
print("function is loading")

check(5)
check(5)
check(5)
check(7)
check(7)

print("function is loading again....please wait")
