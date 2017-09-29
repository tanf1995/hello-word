def bubble_sort(li):
    for i in range(len(li)-1):
        is_sort = True
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                is_sort = False

        if is_sort==True:
            return li

    return li

li1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
li2 = [5, 0, 0, 4, 9, 3, 3, 1]
li3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

li1 = bubble_sort(li1)
li2 = bubble_sort(li2)
li3 = bubble_sort(li3)

print('li1: ', li1)
print('li2: ', li2)
print('li3: ', li3)

# 最好时间复杂度：O（n）
# 最坏时间复杂度：O（n^2）
# 稳定
