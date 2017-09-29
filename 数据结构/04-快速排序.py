def quick_sort(li, start, end):
    if start>=end:
        return

    low = start
    high = end
    mid = li[low]

    while low<high:
        while li[high]>=mid and low<high:
            high -= 1

        li[low] = li[high]

        while li[low]<=mid and low<high:
            low += 1

        li[high] = li[low]

    li[low] = mid

    quick_sort(li, start, low-1)
    quick_sort(li, low+1, end)

li1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
li2 = [5, 0, 0, 4, 9, 3, 3, 1]
li3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

quick_sort(li1, 0, len(li1)-1)
quick_sort(li2, 0, len(li2)-1)
quick_sort(li3, 0, len(li3)-1)

print('li1: ', li1)
print('li2: ', li2)
print('li3: ', li3)

# 最好时间复杂度：O（nlog(n)）
# 最坏时间复杂度：O（n^2）
# 不稳定