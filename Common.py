def count_common(l1, l2):
    l2_copy=[]

    for i in range(len(l2)):
        if l2[i] in l1:
             l2_copy.append(l2[i])
    return l2_copy


l1 = [1, 1, 1,4,3,2,7,8,"raman"]
l2 = [1, 2,8,9,"raman"]
print(count_common(l1, l2))
