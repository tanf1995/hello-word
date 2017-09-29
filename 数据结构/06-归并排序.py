def merge_sort(li):
    if len(li) <= 1:
        return li

    num = len(li)//2
    left = merge_sort(li[:num])
    right = merge_sort(li[num:])

    return merge(left, right)

def merge(left, right):
    i = 0
    j = 0
    res_list = []

    while i<len(left) and j<len(right):
        if left[i] <right[j]:
            res_list.append(left[i])
            i += 1
        else:
            res_list.append(right[j])
            j += 1

    res_list += left[i:]
    res_list += right[j:]

    return res_list

li1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
li2 = [5, 0, 0, 4, 9, 3, 3, 1]
li3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

li1 = merge_sort(li1)
li2 = merge_sort(li2)
li3 = merge_sort(li3)

print('li1: ', li1)
print('li2: ', li2)
print('li3: ', li3)

# 最好时间复杂度：O（nlog(n)）
# 最坏时间复杂度：O（nlog(n)）
# 稳定