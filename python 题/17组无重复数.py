li = [1, 2, 3, 4]

res = []

for th in li:
    for hu in li:
        if th != hu:
            for un in li:
                if un not in (th, hu):
                    item = th*100 + hu*10 + un
                    res.append(item)

print(len(res))
print(res)