import copy

a = [1, 2, 3, 4]

b = a

c = copy.deepcopy(a)

print('创建的列表a的id为%s'%id(a))
print('用浅拷贝---b=a---得b的id为%s'%id(b))
print('用深拷贝---c =copy.deepcopy---得c的id为%s'%id(c))
