def select_sort(li):
    for i in range(len(li)-1):
        min = li[i]
        for j in range(i+1, len(li)):
            if li[j]<min:
                min, li[j] = li[j], min
        li[i] = min

    return li

li1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
li2 = [5, 0, 0, 4, 9, 3, 3, 1]
li3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

li1 = select_sort(li1)
li2 = select_sort(li2)
li3 = select_sort(li3)

print('li1: ', li1)
print('li2: ', li2)
print('li3: ', li3)

# 最好时间复杂度：O（n^2）
# 最坏时间复杂度：O（n^2）
# 不稳定