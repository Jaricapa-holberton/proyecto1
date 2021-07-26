list_num = [12, 3, 4, 5, 6, 7, 10, 11, 8, 2]
list_peak = []
idx = 0
while (idx < len(list_num)):
    if (list_num[idx] > list_num[idx-1] and list_num[idx] >  list_num[idx+1]):
        list_peak.append(list_num[idx])
    idx += 1
print(list_peak)
