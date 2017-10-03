n = int(input())

i = 0
li = []
while i<n:
    li.append(int(input()))
    i += 1

li.sort()

x = -1
ret = 1

for i in range(len(li)):
    if li[i]>0:
        x = i
        break

for i in (x,len(li)):
    if i == ret:
        ret += 1
    else:
        break

print(ret)