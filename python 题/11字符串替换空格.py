# 使用倒序替换的方法，时间复杂度O（n）

st = list(input('输入字符串：'))
rtblank = input('输入替换空格的字符串：')

originaPosNum = len(st)-1

blankNum = 0
for i in range(originaPosNum):
    if st[i] == ' ':
        blankNum += 1

st += [" "]*(len(rtblank)-1)*blankNum
newPosNum = len(st)-1

for i in range(originaPosNum, -1, -1):
    if st[i] != ' ':
        st[newPosNum] = st[i]
        newPosNum -= 1

    else:
        for j in range(len(rtblank)-1, -1, -1):
            st[newPosNum] = rtblank[j]
            newPosNum -= 1

res = ''
for i in st:
    res += i
print(res)

