n, m = map(int, raw_input().split(" "))
li = map(int, raw_input().split(" "))

index = m - 1
count = 0
while True:
    if index < 0:
        index = n-1
    li[index] -= 1
    count += 1
    if li[index] == 0:
        li[index] = count
        break

    index -= 1

res = ''
for i in li:
    res += str(i) + ' '

print res.strip()
