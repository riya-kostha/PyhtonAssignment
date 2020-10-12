sum = 0
count=0
while True:
        num = input("enter no")
        if num == 'q':
            break
        sum += int(num)
        count = count+1


print("average of numbers is ",int(sum/count))