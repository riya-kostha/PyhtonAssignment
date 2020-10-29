def perfectnum(num):

    sum = 0
    for i in range(1,int((num/2)+1)):
        if(num%i==0):
            sum=sum+i

    return(num==sum)
print(perfectnum(14))