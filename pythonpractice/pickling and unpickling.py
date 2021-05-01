import pickle
"""car=["Audi","jaguar","fortuner"]
with open("mycarpickle.txt","wb") as fileobj:
    pickle.dump(car,fileobj)
"""

with open ("mycarpickle.txt","rb") as fileobj:
    print(pickle.load(fileobj))