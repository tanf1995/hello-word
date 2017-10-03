dict1 = {}
dict2 = {}
cha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(1,27):
    dict1[cha[i-1]] = i
    dict2[i] = cha[i-1]

n = int(input())

li1 = []
li2 = []  #0代表栅格格式，1代表行列格式
for i in range(n):
    temp = input()
    if temp[0]=='R' and 'C' in temp and temp.index('R')!=temp.index('C')-1:
        try:
            for j in range(temp.index('R')+1, temp.index('C')):
                int(temp[j])
        except Exception:
            li2.append(0)
        else:
            li2.append(1)


    else:
        li2.append(0)

    li1.append(temp)

res = []

for i in range(len(li1)):
    if li2[i]==0:
        tup_temp = []
        for j in range(len(li1[i])):
            try:
                int(li1[i][j])
            except Exception:
                pass
            else:
                tup_temp = [li1[i][:j], li1[i][j:]]
                break

        length = len(tup_temp[0])
        num = 0
        for x in range(length):
            num += int(dict1[tup_temp[0][x]])*(26**(length-1-x))

        res.append('R'+tup_temp[1]+'C'+str(num))

    else:
        row = li1[i][1:li1[i].index('C')]
        col = int(li1[i][li1[i].index('C')+1:])
        num = ''

        while True:
            if col//26!=0:
                low = col%26
                value = dict2[low]
                num = value + num
                col = col//26
            else:
                value = dict2[col]
                num = value + num
                break

        res.append(num+str(row))

for item in res:
    print(item)
