def searcher():
    import time
    book="this book belongs to pulkit and john"
    time.sleep(4)
    print(book)


    while True:
        text=(yield )
        if text in book:
            print("this is in book")
        else:
            print("this is not in book")
search=searcher()
next(search)
search.send("pulkit")
input("press key")
search.send("pulkit and")
input("press key")
search.send("pulkit and john")


