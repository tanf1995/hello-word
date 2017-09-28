import copy

a = [[1], [2], [3]]

b = copy.copy(a)

print('--对b使用copy.copy后')

print('--id(a)-->>%s'%id(a))
print('--id(b)-->>%s'%id(b))
print('--id(a[0])-->>%s'%id(a[0]))
print('--id(b[0])-->>%s'%id(b[0]))
