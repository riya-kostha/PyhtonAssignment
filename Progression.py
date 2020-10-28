

def progression(l1):
    dif = l1[1] - l1[0];

    for i in range(len(l1) - 1):
     
        if not (l1[i+1]-l1[i]==dif):

            return  False
    return  True


l1=[5,7,9,8]
print(progression(l1))