li = [1, 2, 3, 1, 2, 3, 2, 4]

dic = dict.fromkeys(li, 0)  # 转换为字典，设值为0

for i in li:
    dic[i] += 1

tup = [(k, v) for k, v in dic.items()]

for i in range(len(tup)-1):
    is_sort = True
    for j in range(len(tup)-i-1):
        if tup[j][1] < tup[j+1][1]:
            tup[j], tup[j+1] = tup[j+1], tup[j]
            is_sort = False

        elif tup[j][1] == tup[j+1][1] and tup[j][0] < tup[j+1][0]:
            tup[j], tup[j + 1] = tup[j + 1], tup[j]
            is_sort = False
            
    if is_sort:
        break

print(tup)
res = []
for i in tup:
    res.append(i[0])

print(res)