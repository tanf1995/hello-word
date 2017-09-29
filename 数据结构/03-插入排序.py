def insert_sort(li):
    for i in range(1, len(li)):
        for j in range(i, 0, -1):
            if li[j]<li[j-1]:
                li[j], li[j-1] = li[j-1], li[j]
            else:
                break

    return li

li1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
li2 = [5, 0, 0, 4, 9, 3, 3, 1]
li3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

li1 = insert_sort(li1)
li2 = insert_sort(li2)
li3 = insert_sort(li3)

print('li1: ', li1)
print('li2: ', li2)
print('li3: ', li3)

# 最好时间复杂度：O（n）
# 最坏时间复杂度：O（n^2）
# 稳定