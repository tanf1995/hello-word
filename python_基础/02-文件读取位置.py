f = open('test.txt', 'r')

str1 = f.read(3)

print('读取内容是：', str1)
print('读取位置是：', f.tell())

str2 = f.read(3)


print('读取内容是：', str2)
print('读取位置是：', f.tell())
