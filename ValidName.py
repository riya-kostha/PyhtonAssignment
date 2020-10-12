while True:
        name = input("enter name")
        if  name.isprintable() and len(name)>=5 and name.isascii() :
            print("name is",name)
            break
