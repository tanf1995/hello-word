n = int(raw_input())
li = map(int, raw_input().split(','))

max_num1 = max(li)
max_num2 = max(li)
max_num3 = max(li)
max_num_index = li.index(max_num1)

if max_num_index == n-1:
    act_index1 = 0
else:
    act_index1 = max_num_index + 1
sum_num1 = max_num1

while True:
    if act_index1 == max_num_index:
        break

    sum_num1 = sum_num1 + li[act_index1]
    if act_index1 < n-1:
        act_index1 += 1
    else:
        act_index1 = 0

    if sum_num1 > max_num1:
        max_num1 = sum_num1

if max_num_index == 0:
    act_index2 = n-1
else:
    act_index2 = max_num_index - 1
sum_num2 = max_num2

while True:
    if act_index2 == max_num_index:
        break

    sum_num2 = sum_num2 + li[act_index2]
    if act_index2 > 0:
        act_index2 -= 1
    else:
        act_index2 = n-1

    if sum_num2 > max_num2:
        max_num2 = sum_num2

if max_num_index == n-1:
    act_index1 = 0
    act_index2 = n-2
elif max_num_index == 0:
    act_index2 = n-1
    act_index1 = 1
else:
    act_index1 = max_num_index + 1
    act_index2 = max_num_index - 1
sum_num3 = max_num3

while True:
    if act_index2 == act_index1:
        break

    sum_num3 = sum_num3 + li[act_index2]
    if act_index2 > 0:
        act_index2 -= 1
    else:
        act_index2 = n-1

    if sum_num3 > max_num3:
        max_num3 = sum_num3

    sum_num3 = sum_num3 + li[act_index1]
    if act_index1 < n - 1:
        act_index1 += 1
    else:
        act_index1 = 0

    if sum_num3 > max_num3:
        max_num3 = sum_num3

res = max(max_num1, max_num2, max_num3)
print res

