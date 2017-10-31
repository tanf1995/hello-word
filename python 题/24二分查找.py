li = [x for x in range(100)]

num = int(input('查找的数>>'))


low = 0
high = len(li) - 1

while True:
    mid = (high - low)//2 + low

    if high < low:
        print('不存在')
        break

    if li[mid] > num:
        high = mid - 1
        print('查找中，小于%d'%li[mid])

    if li[mid] < num:
        low = mid + 1
        print('查找中, 大于%d'%li[mid])

    if li[mid] == num:
        print('找到了')
        break
