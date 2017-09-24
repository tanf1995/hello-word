list1 = input().split(" ")
n = int(list1[0])
m = int(list1[1])

list2 = list(map(int, input().split(" ")))

newList = []
for i in range(n-1):
    numb = str(bin(list2[i]))[2:]
    for j in range(i+1, n):
        num2b = str(bin(list2[j]))[2:]
        
        if len(numb) > len(num2b):
            max_po = len(numb)
            min_po = len(num2b)
        else:
            max_po = len(num2b)
            min_po = len(numb)
        newNum = ''
        for i in range(min_po):
            if numb[-1-i] != num2b[-1-i]:
                newNum = '1' + newNum
            else:
                newNum = '0' + newNum
        newNum = '1'*(max_po-min_po) + newNum
        newList.append(int(newNum, 2))
        
ans = 0
for i in newList:
    if i > m:
        ans += 1
        
print(ans)