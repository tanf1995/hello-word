str1 = input()

j=0
list1 = []
for i in str1:
    if i == " ":
        list1.append(j)
        j += 1

    else:
        list1.append(i)

list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)

res = ''
for i in list2:
    if type(i) == type(1):
        res += " "
    else:
        res += i

res += "\""
print(res)