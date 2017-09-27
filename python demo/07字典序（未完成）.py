n = int(input())
m = int(input())

li = [x for x in range(1,n+1)]

st = list(map(str, li))

liws = []

liws.append(li[0:9])
for i in range(1,len(str(n))):
    item = li[int('9'*i):int('9'*(i+1))]
    liws.append(item)

res = []
tier = len(liws)
tree = []





