n1 = int(input())
li1 = list(map(int, input().split(" ")))

n2 = int(input())
li2 = list(map(int, input().split(" ")))

li = li1 + li2
new_li = []
for i in li:
    if i not in new_li:
        new_li.append(i)

new_li.sort()

length = len(new_li)
if length%2 == 0:
    mid = length//2
    res = (new_li[mid-1] + new_li[mid])/2

else:
    mid = length//2
    res = new_li[mid]

print(res)
