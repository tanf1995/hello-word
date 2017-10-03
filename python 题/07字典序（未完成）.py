li = [i for i in range(1,25)]

pos = len(str(li[-1]))

li_d = [[]]*pos


for i in range(pos):
    li_d[i] = li[10**i-1:10**(i+1)-1]


res = []
def pushIn(i, res):
    if i<pos-1:
        for j in range(1, 10):
            res.append(li_d[i][j-1])
            i+=1
            pushIn(i, res)

    elif i==pos-1:
        for j in range(1, 10):
            res += li_d[i][(j-1)*10:j*10]
    return res

resu = pushIn(0, res)
print(resu[:15])



# for i in range(1,10):
#     res.append(li_1[0][i-1])
#     for j in range(1,10):
#         res.append(li_1[1][j-1])
#         res += li_1[2][(j-1)*10:j*10]

# print(res[:21])




