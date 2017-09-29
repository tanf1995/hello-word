def shell_sort(li):
    leng = len(li)
    gap = leng//2

    while gap>0:
        for i in range(gap, leng):
            j = i
            while j>=gap and li[j]<li[j-gap]:
                li[j], li[j-gap] = li[j-gap], li[j]
                j -= gap

        gap = gap//2

    return li

li1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
li2 = [5, 0, 0, 4, 9, 3, 3, 1]
li3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

li1 = shell_sort(li1)
li2 = shell_sort(li2)
li3 = shell_sort(li3)

print('li1: ', li1)
print('li2: ', li2)
print('li3: ', li3)

# 最好时间复杂度：随步长不同
# 最坏时间复杂度：O（n^2）
# 不稳定
