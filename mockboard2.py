list1 = [[1, 5, 8],[2, 7, 98],[3, 10, 11]]
list2 = []
idx1 = 0
idx2 = 0
while(idx1 < len(list1)):
    while(idx2 < len(list1[idx1])):
        list2.append(list1[idx1][idx2])
        idx2 += 1
    idx2 = 0
    idx1 += 1
list2.sort()
print(list2)