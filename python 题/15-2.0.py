n, m = map(int, raw_input().split(" "))
li = map(int, raw_input().split(" "))

m = m-1
go_times = min(li)

li_index = []
for i in range(n):
    if li[i] == min(li):
        li_index.append(i)

li_bac = []
for i in li:
    li_bac.append(i)

for index in li_index:
    is_ok = True
    if m < index:
        for i in range(n):
            li[i] -= go_times
            if li[i] < 0:
                is_ok = False
                break
        if not is_ok:
            li = []
            for i in li_bac:
                li.append(i)
            continue
        for i in range(index+1, n):
            li[i] -= 1
            if li[i] < 0:
                is_ok = False
                break
        if not is_ok:
            li = []
            for i in li_bac:
                li.append(i)
            continue
        for i in range(m+1):
            li[i] -= 1
            if li[i] < 0:
                is_ok = False
                break
        if not is_ok:
            li = []
            for i in li_bac:
                li.append(i)
            continue
        li[index] = go_times * n + (n - index + m)
    else:
        for i in range(n):
            li[i] -= go_times
            if li[i] < 0:
                is_ok = False
                break
        if not is_ok:
            li = []
            for i in li_bac:
                li.append(i)
            continue
        for i in range(index+1, m+1):
            li[i] -= 1
            if li[i] < 0:
                is_ok = False
                break
        if not is_ok:
            li = []
            for i in li_bac:
                li.append(i)
            continue
        li[index] = go_times * n + (m - index)

    res = ''
    for i in li:
        res += str(i) + ' '
    print res.strip()
    break