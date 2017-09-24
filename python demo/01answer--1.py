n = int(input())
a = list(map(int, input().split(' ')))
a.sort()
ans = 0
num = 0
for x in a:
    num %= 3
    if num != 0 and x > last + 10:
        ans += 3 - num
        num = 0
    num += 1
    last = x
ans += 3 - num
print(ans)