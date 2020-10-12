sum = 0
n = int(input("enter no"))
for x in range(1, n):
    if x%3 != 0 and x % 7 != 0 and x % 17 != 0:
        sum += x


print(sum)