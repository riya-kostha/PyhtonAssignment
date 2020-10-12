list=[1,2,45,67,89,90,170]
for i in range(len(list)):
    list.sort()

print("list is",list)
print("second largest number",list.__getitem__(len(list)-2))
print("second smallest number",list.__getitem__(1))