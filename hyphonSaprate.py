def hyphon(str):
    arr = str.split('-')
    arr = sorted(arr)
    return '-'.join(arr)

s = input("enter string")
print (hyphon(s))
