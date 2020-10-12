list=[];
for i in range(71,82):
    list.append(i)

print("First lis is:",list)

list2=[]
for i in range(len(list)):
    list2.append(list.__getitem__(i)*list.__getitem__(i))


print("First lis is:",list2)