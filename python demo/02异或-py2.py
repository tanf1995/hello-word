list1 = raw_input().split(" ")
n = int(list1[0])
m = int(list1[1])

list2 = map(int, raw_input().split(" "))

newList = []
for i in range(n-1):
    for j in range(i+1, n):
        newList.append(list2[i]^list2[j])
        
ans = 0
for i in newList:
    if i > m:
        ans += 1
        
print ans