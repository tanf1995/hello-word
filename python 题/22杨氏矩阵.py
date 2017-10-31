n, m = list(map(int, input('输入矩阵行数和列数， 如2,3\n>>').split(',')))
num = int(input('输入判断是否在矩阵中的数\n>>'))

is_exist = False
li = []
for i in range(n):
    li.append([])

for i in range(1, n+1):
    for j in range(1, m+1):
       item = j+i-1
       if item == num:
           is_exist = True
       li[i-1].append(item)

print(li)

if is_exist:
    print('存在')
else:
    print('不存在')