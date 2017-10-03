# coding=utf-8

def str_find(source, target):
    num = source.find(target)
    return num

strs = input().split(' ')
source = strs[0]
target = strs[1]

res = str_find(source, target)
print(res)