def merge_sort(li1, li2, res=[]):
    if not li1 or not li2:
        res.extend(li1)
        res.extend(li2)
        return res

    if li1[0] < li2[0]:
        res.append(li1[0])
        del li1[0]
    else:
        res.append(li2[0])
        del li2[0]

    return merge_sort(li1, li2, res)

li1 = [1, 3, 5, 7]
li2 = [2, 4, 6, 8]

res = merge_sort(li1, li2)
print(res)