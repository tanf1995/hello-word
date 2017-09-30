def steps(n, cur):
    # count for which less than n and begin with cur
    step = 0
    maxi = cur + 1
    while cur <= n:    #n是总数
        if maxi <= n:
            step += maxi - cur
        else:
            step += n - cur + 1
        cur *= 10
        maxi *= 10
    return step


li = list(map(int, input().split()))
n = li[0]
m = li[1]

cur = 1
while m > 1:
    step = steps(n, cur)
    if step < m:
        cur += 1
        m -= step
    else:
        cur *= 10
        m -= 1

print(cur)